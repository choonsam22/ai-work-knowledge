#!/usr/bin/env python3
"""
현재 상태를 사람이 읽기 좋게 출력. (JSONL을 직접 읽을 필요 없게)

사용법:
  python coordination/status.py                 # 전체 요약
  python coordination/status.py --queue          # 조사 큐만
  python coordination/status.py --debates        # 토론 대기 중인 것만
  python coordination/status.py --pending-human  # 사람 승인 대기 (judge가 adopt 판정한 것)
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import derive_state, git  # noqa: E402


def print_queue(state):
    if not state:
        print("(등록된 조사 항목 없음)")
        return
    for tid, t in sorted(state.items()):
        grade = f" grade={t['source_grade']}" if t["source_grade"] else ""
        print(f"  [{t['status']:>13}] {tid}  owner={t['owner']:<6} "
              f"company={t['company']} area={t['work_area']} case={t['use_case']}{grade}")


def print_debates(state, debates):
    open_debates = {tid: d for tid, d in debates.items() if d["verdict"] is None}
    if not open_debates:
        print("(판정 대기 중인 토론 없음)")
        return
    for tid, d in open_debates.items():
        t = state.get(tid, {})
        print(f"  - {tid} (조사자: {t.get('owner')}, company={t.get('company')})")
        for r in d["reasons"]:
            claim = f" | 주장: {r['claim']}" if r.get("claim") else ""
            print(f"      제기자={r['by']}: {r['reason']}{claim}")
        involved = {t.get("owner")} | {r["by"] for r in d["reasons"]}
        available_judges = {"claude", "codex", "agy"} - involved
        print(f"      => 판정 가능한 AI: {sorted(available_judges)}")


def print_pending_human(state, debates):
    pending = [(tid, d["verdict"]) for tid, d in debates.items()
               if d["verdict"] and d["verdict"]["decision"] == "adopt"]
    if not pending:
        print("(사람 승인 대기 중인 항목 없음)")
        return
    for tid, v in pending:
        t = state.get(tid, {})
        print(f"  - {tid}: {t.get('company')} / {t.get('use_case')}")
        print(f"      AI 판정: adopt (judge={v['judge']}) - {v['reasoning']}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--queue", action="store_true")
    p.add_argument("--debates", action="store_true")
    p.add_argument("--pending-human", action="store_true")
    p.add_argument("--no-pull", action="store_true")
    args = p.parse_args()

    if not args.no_pull:
        git("pull", "--rebase", "origin", "main", check=False)

    state, debates = derive_state()

    show_all = not (args.queue or args.debates or args.pending_human)

    if args.queue or show_all:
        print("=== 조사 큐 ===")
        print_queue(state)
        print()
    if args.debates or show_all:
        print("=== 판정 대기 중인 토론 ===")
        print_debates(state, debates)
        print()
    if args.pending_human or show_all:
        print("=== 사람(이상민 과장) 최종 승인 대기 (AI가 adopt 판정) ===")
        print_pending_human(state, debates)


if __name__ == "__main__":
    main()
