#!/usr/bin/env python3
"""
check_duplicate.py 통과 후, 조사를 시작하기 전에 실행.
이벤트를 append하고 '즉시' commit+push해서 다른 AI가 바로 볼 수 있게 한다.

사용법:
  python coordination/reserve.py --owner claude --company "Hyundai Steel" \
      --area "경영지원" --case "SAIP 챗봇" --alias 현대제철
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import (VALID_OWNERS, append_event, find_duplicates, git,  # noqa: E402
                  push_with_retry, slugify_id)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--owner", required=True, choices=sorted(VALID_OWNERS))
    p.add_argument("--company", required=True)
    p.add_argument("--area", required=True)
    p.add_argument("--case", required=True)
    p.add_argument("--alias", action="append", default=[])
    p.add_argument("--url", action="append", default=[])
    p.add_argument("--force", action="store_true", help="중복 검사 건너뛰기 (권장 안 함)")
    args = p.parse_args()

    git("pull", "--rebase", "origin", "main", check=False)

    if not args.force:
        real_dups = [m for m in find_duplicates(args.company, args.area, args.case, args.url)
                     if not m.get("same_company_different_angle")]
        if real_dups:
            print("[중단] 중복 가능성이 있습니다. 먼저 check_duplicate.py로 확인하세요.")
            for m in real_dups:
                print(f"  - id={m['id']} owner={m['owner']} status={m['status']}")
            sys.exit(1)

    tid = slugify_id(args.company, args.case)
    event = {
        "type": "RESERVE",
        "id": tid,
        "owner": args.owner,
        "company": args.company,
        "aliases": args.alias,
        "work_area": args.area,
        "use_case": args.case,
        "source_urls": args.url,
    }
    append_event(event)
    ok, msg = push_with_retry(f"reserve: {tid} ({args.owner})", ["coordination/events.jsonl"])
    if not ok:
        print(f"[경고] 커밋은 됐지만 push 실패: {msg}")
        print("=> 예약이 다른 AI에게 아직 안 보입니다. 수동으로 git push 해주세요.")
        sys.exit(2)

    print(f"[예약 완료] id={tid} owner={args.owner}")
    print(f"조사 결과는 findings/{args.owner}/{tid}.md 에 저장한 뒤 아래로 완료 처리하세요:")
    print(f'  python coordination/complete.py --id {tid} --file findings/{args.owner}/{tid}.md '
          f'--grade A|B|C --url <출처URL>')


if __name__ == "__main__":
    main()
