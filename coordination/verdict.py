#!/usr/bin/env python3
"""
FLAG_DEBATE 된 건에 대해 '논쟁에 참여하지 않은' 제3의 AI가 판정을 기록.
judge는 원 조사자(owner)나 이의제기자(by)와 달라야 함 (스크립트가 강제 검사).

decision: adopt(채택) / hold(보류, 추가확인 필요) / exclude(제외) / needs_more_research(재조사 필요)

주의: 여기서 adopt/exclude가 나와도 '최종 임원보고 반영 여부'는 사람 확인을 거쳐야 함.
      이 스크립트는 AI 간 판정만 기록하고, 최종 채택 여부는 decisions_for_human.md 에서
      사람이 별도로 승인 표시를 남긴다.

사용법:
  python coordination/verdict.py --id ABB-GENIX-COPILOT --judge agy \
      --decision hold --reasoning "40% 수치의 산출 기준이 불명확 - ABB 1차 자료로 재확인 필요"
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import append_event, derive_state, git, push_with_retry  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--id", required=True)
    p.add_argument("--judge", required=True, choices=["claude", "codex", "agy"])
    p.add_argument("--decision", required=True,
                   choices=["adopt", "hold", "exclude", "needs_more_research"])
    p.add_argument("--reasoning", required=True, help="판정 근거 1~2줄")
    args = p.parse_args()

    git("pull", "--rebase", "origin", "main", check=False)

    state, debates = derive_state()
    if args.id not in state:
        print(f"[오류] id={args.id} 가 존재하지 않습니다.")
        sys.exit(1)
    if args.id not in debates:
        print(f"[오류] id={args.id} 는 FLAG_DEBATE 된 적이 없습니다. flag_debate.py 먼저 실행하세요.")
        sys.exit(1)

    owner = state[args.id]["owner"]
    disputers = {r["by"] for r in debates[args.id]["reasons"]}
    involved = {owner} | disputers
    if args.judge in involved:
        print(f"[중단] '{args.judge}' 는 이 건의 조사자 또는 이의제기자라 심판을 맡을 수 없습니다.")
        print(f"       관련자: {involved} / 참여하지 않은 AI가 판정해야 합니다.")
        sys.exit(1)

    append_event({
        "type": "DEBATE_VERDICT",
        "id": args.id,
        "judge": args.judge,
        "decision": args.decision,
        "reasoning": args.reasoning,
    })
    ok, msg = push_with_retry(f"verdict: {args.id} -> {args.decision} (judge={args.judge})",
                               ["coordination/events.jsonl"])
    if not ok:
        print(f"[경고] push 실패: {msg}")
        sys.exit(2)

    print(f"[판정 기록] id={args.id} decision={args.decision} judge={args.judge}")
    if args.decision == "adopt":
        print("=> 최종 임원보고 반영 여부는 이상민 과장님 확인이 필요합니다 (AI 판정만으로 자동 확정 아님).")


if __name__ == "__main__":
    main()
