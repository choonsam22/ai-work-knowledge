#!/usr/bin/env python3
"""
조사 완료 후 실행. 결과 파일 경로와 출처 등급을 기록하고 push.

사용법:
  python coordination/complete.py --id HYUNDAI-STEEL-SAIP --file findings/claude/HYUNDAI-STEEL-SAIP.md \
      --grade C --url https://... --flag-debate "출처가 PR Newswire뿐이라 재검증 필요"
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import append_event, derive_state, git, push_with_retry  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--id", required=True)
    p.add_argument("--file", required=True, help="findings/<owner>/<id>.md 경로")
    p.add_argument("--grade", required=True, choices=["A", "B", "C"], help="출처 신뢰도")
    p.add_argument("--url", action="append", default=[])
    p.add_argument("--owner", required=True, choices=["claude", "codex", "agy"],
                   help="FLAG_DEBATE 기록 시 누구 명의인지")
    p.add_argument("--flag-debate", default=None,
                   help="이 값을 주면 자동으로 토론 대상으로 등록 (사유 텍스트)")
    args = p.parse_args()

    git("pull", "--rebase", "origin", "main", check=False)

    state, _ = derive_state()
    if args.id not in state:
        print(f"[오류] id={args.id} 가 RESERVE 되어있지 않습니다. reserve.py 먼저 실행하세요.")
        sys.exit(1)

    if not Path(args.file).exists():
        print(f"[경고] {args.file} 파일이 아직 없습니다. 먼저 조사 결과를 저장하세요.")
        sys.exit(1)

    append_event({
        "type": "COMPLETE",
        "id": args.id,
        "status": "done",
        "file": args.file,
        "source_grade": args.grade,
        "source_urls": args.url,
    })

    paths = ["coordination/events.jsonl", args.file]

    # C등급이면 자동으로 토론 후보 플래그 (사유 미지정이어도 등급만으로 플래그)
    reason = args.flag_debate
    if reason is None and args.grade == "C":
        reason = "출처 등급 C - 공식발표/1차자료 재검증 필요"
    if reason:
        append_event({
            "type": "FLAG_DEBATE",
            "id": args.id,
            "by": args.owner,
            "reason": reason,
            "claim": None,
        })

    ok, msg = push_with_retry(f"complete: {args.id} (grade={args.grade})", paths)
    if not ok:
        print(f"[경고] push 실패: {msg}")
        sys.exit(2)

    print(f"[완료] id={args.id} 저장 및 push 완료.")
    if reason:
        print(f"[토론 대상으로 등록됨] 사유: {reason}")
        print("다른 AI가 coordination/status.py --debates 로 확인 후 반론/검증할 수 있습니다.")


if __name__ == "__main__":
    main()
