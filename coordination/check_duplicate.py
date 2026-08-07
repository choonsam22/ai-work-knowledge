#!/usr/bin/env python3
"""
조사를 시작하기 전에 반드시 먼저 실행.

사용법:
  python coordination/check_duplicate.py --company "Hyundai Steel" --area "경영지원" --case "SAIP 챗봇" [--url https://...]

git pull까지 자동으로 해서 최신 상태 기준으로 검사한다.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import find_duplicates, git  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--company", required=True)
    p.add_argument("--area", required=True, help="업무영역 (예: 영업/구매/재무/HR/기획/법무)")
    p.add_argument("--case", required=True, help="구체적 사례 (예: 영업 Copilot, Invoice 검증)")
    p.add_argument("--url", action="append", default=[], help="참고 출처 URL (여러 개 가능)")
    p.add_argument("--no-pull", action="store_true", help="git pull 생략 (디버그용)")
    args = p.parse_args()

    if not args.no_pull:
        result = git("pull", "--rebase", "origin", "main", check=False)
        if result.returncode != 0:
            print("[경고] git pull 실패 - 로컬에 커밋 안 된 변경사항이 있는지 확인하세요.")
            print(result.stderr)

    matches = find_duplicates(args.company, args.area, args.case, args.url)
    real_dups = [m for m in matches if not m.get("same_company_different_angle")]
    same_company_diff_angle = [m for m in matches if m.get("same_company_different_angle")]

    if real_dups:
        print(f"[중복 가능성 높음] '{args.company}' / '{args.area}' / '{args.case}' 와 겹치는 항목 {len(real_dups)}건:")
        for m in real_dups:
            print(f"  - id={m['id']} owner={m['owner']} status={m['status']} "
                  f"(회사유사도={m['company_similarity']}, 영역/사례유사도={m['area_case_similarity']}, url일치={m['url_match']})")
        print("\n=> 다른 업무영역/사례가 아니라면 이 조사는 진행하지 말고 다른 후보를 고르세요.")
        sys.exit(1)

    if same_company_diff_angle:
        print(f"[참고] 같은 회사지만 다른 업무영역/사례라 중복 아님 (진행 가능):")
        for m in same_company_diff_angle:
            print(f"  - id={m['id']} owner={m['owner']} area={m['work_area']} case={m['use_case']}")

    print(f"\n[OK] 중복 없음. 아래 명령으로 예약하세요:")
    print(f'  python coordination/reserve.py --owner <claude|codex|agy> --company "{args.company}" '
          f'--area "{args.area}" --case "{args.case}"')


if __name__ == "__main__":
    main()
