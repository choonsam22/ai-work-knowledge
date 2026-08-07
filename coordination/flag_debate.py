#!/usr/bin/env python3
"""
이미 완료된 항목에 대해, 다른 AI가 나중에 이의를 제기할 때 사용.
(출처 등급 C는 complete.py에서 자동으로 플래그되므로 여기선 나머지 4가지 트리거만 다룸)

트리거 기준 (이 중 하나라도 해당하면 플래그):
  - 출처가 약함 (등급 C, 홍보성 자료뿐)
  - 정량 수치의 의미/원인이 불명확함 (생성AI 효과인지 기존 자동화 효과인지 혼재)
  - 세아제강과의 관련성이 논쟁적임 (관리부문 사무직 vs 현장/엔지니어링 성격)
  - 같은 사례를 다른 AI가 조사했는데 결론(Level, 관련성 등)이 크게 다름

사용법:
  python coordination/flag_debate.py --id ABB-GENIX-COPILOT --by codex \
      --reason "O&M 비용 40% 감소가 생성AI만의 효과인지 불명확" \
      --claim "생성AI 단독 효과로 보기 어려움, 기존 Genix 분석 시스템 효과 혼재 가능성"
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import append_event, derive_state, git, push_with_retry  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--id", required=True)
    p.add_argument("--by", required=True, choices=["claude", "codex", "agy"])
    p.add_argument("--reason", required=True)
    p.add_argument("--claim", default=None, help="구체적으로 어떤 부분이 문제인지 1~2줄 주장")
    args = p.parse_args()

    git("pull", "--rebase", "origin", "main", check=False)

    state, _ = derive_state()
    if args.id not in state:
        print(f"[경고] id={args.id} 가 존재하지 않습니다. 오타 확인하세요.")
        sys.exit(1)

    append_event({
        "type": "FLAG_DEBATE",
        "id": args.id,
        "by": args.by,
        "reason": args.reason,
        "claim": args.claim,
    })
    ok, msg = push_with_retry(f"flag_debate: {args.id} (by {args.by})", ["coordination/events.jsonl"])
    if not ok:
        print(f"[경고] push 실패: {msg}")
        sys.exit(2)
    print(f"[플래그 등록] id={args.id} by={args.by}")
    print("이 건에 참여하지 않은 세 번째 AI가 coordination/verdict.py 로 판정해야 합니다.")


if __name__ == "__main__":
    main()
