"""
coordination/lib.py

3개 AI(Codex/Claude/agy-Gemini)가 각자 별도 터미널에서 이 저장소를 clone해 작업할 때,
공유 이벤트 로그(events.jsonl)를 append-only로 주고받아 중복 조사를 막고
선택적 토론이 필요한 시점만 걸러내기 위한 공통 라이브러리.

의존성 없음 (표준 라이브러리만 사용) - Codex/agy 등 다른 환경에서도 그대로 동작하도록.
"""
import json
import re
import subprocess
import sys
import time
import unicodedata
import uuid
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_PATH = REPO_ROOT / "coordination" / "events.jsonl"

VALID_OWNERS = {"claude", "codex", "agy"}
VALID_TYPES = {"RESERVE", "COMPLETE", "ABANDON", "FLAG_DEBATE", "DEBATE_VERDICT"}


def now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%S+09:00", time.localtime())


def normalize(text: str) -> str:
    """대소문자/공백/특수문자 무시하고 비교하기 위한 정규화."""
    if not text:
        return ""
    text = unicodedata.normalize("NFKC", text).lower()
    text = re.sub(r"[^\w가-힣]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def token_overlap(a: str, b: str) -> float:
    """두 문자열의 토큰 자카드 유사도 (0~1). 회사명/업무영역/사례 비교용 단순 휴리스틱."""
    ta, tb = set(normalize(a).split()), set(normalize(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def load_events():
    if not EVENTS_PATH.exists():
        return []
    events = []
    with open(EVENTS_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                events.append(json.loads(line))
    return events


def append_event(event: dict):
    event.setdefault("ts", now_iso())
    event.setdefault("event_id", str(uuid.uuid4())[:8])
    EVENTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(EVENTS_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")
    return event


def derive_state():
    """
    이벤트 로그를 처음부터 재생해서 현재 상태를 계산.
    반환: { task_id: {company, work_area, use_case, owner, status, source_urls, ...} }
    """
    state = {}
    debates = {}
    for ev in load_events():
        etype = ev.get("type")
        tid = ev.get("id")
        if etype == "RESERVE":
            state[tid] = {
                "id": tid,
                "company": ev.get("company", ""),
                "aliases": ev.get("aliases", []),
                "work_area": ev.get("work_area", ""),
                "use_case": ev.get("use_case", ""),
                "owner": ev.get("owner", ""),
                "status": "investigating",
                "source_urls": ev.get("source_urls", []),
                "reserved_at": ev.get("ts"),
                "file": None,
                "source_grade": None,
            }
        elif etype == "COMPLETE" and tid in state:
            state[tid]["status"] = ev.get("status", "done")
            state[tid]["file"] = ev.get("file")
            state[tid]["source_grade"] = ev.get("source_grade")
            state[tid]["source_urls"] = ev.get("source_urls", state[tid]["source_urls"])
        elif etype == "ABANDON" and tid in state:
            state[tid]["status"] = "abandoned"
        elif etype == "FLAG_DEBATE":
            debates.setdefault(tid, {"reasons": [], "claims": [], "verdict": None})
            debates[tid]["reasons"].append(
                {"by": ev.get("by"), "reason": ev.get("reason"), "claim": ev.get("claim")}
            )
        elif etype == "DEBATE_VERDICT":
            debates.setdefault(tid, {"reasons": [], "claims": [], "verdict": None})
            debates[tid]["verdict"] = {
                "judge": ev.get("judge"),
                "decision": ev.get("decision"),  # adopt / hold / exclude / needs_more_research
                "reasoning": ev.get("reasoning"),
                "ts": ev.get("ts"),
            }
    return state, debates


def find_duplicates(company: str, work_area: str, use_case: str, source_urls=None, threshold=0.5):
    """
    후보 조사 항목이 기존에 이미 있는지 검사.
    키: 회사(+aliases) + 업무영역 + 사례 + 출처URL 조합.
    같은 회사라도 업무영역/사례가 다르면 중복이 아님 (예: 영업 Copilot vs 재무 자동화).
    """
    source_urls = source_urls or []
    state, _ = derive_state()
    matches = []
    for tid, task in state.items():
        if task["status"] == "abandoned":
            continue
        company_names = [task["company"]] + task.get("aliases", [])
        company_sim = max(token_overlap(company, c) for c in company_names) if company_names else 0.0
        if company_sim < 0.5:
            continue
        # 출처 URL이 완전히 같으면 사실상 같은 사례
        url_hit = bool(set(source_urls) & set(task.get("source_urls", [])))
        area_sim = token_overlap(work_area, task["work_area"])
        case_sim = token_overlap(use_case, task["use_case"])
        # area가 한쪽이라도 비어있으면(레거시 백필 등) case 유사도만으로 판단.
        # 둘 다 있으면 area+case 평균 (업무영역이 다르면 같은 회사라도 다른 사례일 수 있으므로).
        if not work_area or not task["work_area"]:
            content_sim = case_sim
        else:
            content_sim = (area_sim + case_sim) / 2
        combined = url_hit or content_sim >= threshold
        if combined:
            matches.append({
                "id": tid,
                "company": task["company"],
                "work_area": task["work_area"],
                "use_case": task["use_case"],
                "owner": task["owner"],
                "status": task["status"],
                "company_similarity": round(company_sim, 2),
                "area_case_similarity": round(content_sim, 2),
                "url_match": url_hit,
            })
        else:
            # 회사는 같은데 업무영역/사례가 다름 -> 중복 아님, 참고용으로만 보여줌
            matches.append({
                "id": tid,
                "company": task["company"],
                "work_area": task["work_area"],
                "use_case": task["use_case"],
                "owner": task["owner"],
                "status": task["status"],
                "company_similarity": round(company_sim, 2),
                "area_case_similarity": round(content_sim, 2),
                "url_match": False,
                "same_company_different_angle": True,
            })
    return matches


def slugify_id(company: str, use_case: str) -> str:
    base = re.sub(r"[^A-Za-z0-9가-힣]+", "-", f"{company}-{use_case}").strip("-").upper()
    base = re.sub(r"-+", "-", base)
    return base[:60]


def git(*args, check=True):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, check=check,
        encoding="utf-8", errors="replace",
    )


def push_with_retry(commit_message: str, paths, max_retries=3):
    """
    이벤트 로그는 append-only라 병합 충돌 가능성이 낮지만,
    동시에 여러 AI가 push할 수 있으므로 pull --rebase 후 재시도.
    """
    for attempt in range(1, max_retries + 1):
        git("add", *paths)
        commit = git("commit", "-m", commit_message, check=False)
        if commit.returncode != 0:
            combined = commit.stdout + commit.stderr
            if "nothing to commit" in combined:
                return True, "nothing to commit"
            # 커밋 자체가 실패한 경우(예: git identity 미설정) push로 넘어가면 안 됨 —
            # push가 우연히 성공(Everything up-to-date)해서 거짓 성공을 보고하는 버그 방지
            return False, f"commit 실패: {combined.strip()}"
        push = git("push", "origin", "main", check=False)
        if push.returncode == 0:
            return True, push.stdout
        # push 실패 -> 최신 내용 받아서 재시도
        git("pull", "--rebase", "origin", "main", check=False)
        time.sleep(1)
    return False, f"push 실패: {max_retries}회 재시도 후 포기. 수동으로 git status 확인 필요."
