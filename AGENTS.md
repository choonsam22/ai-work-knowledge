# 이 저장소에서 작업하는 AI(Codex / Claude / agy-Gemini)를 위한 프로토콜

이 저장소는 세아제강 관리부문 AI 생산성 벤치마킹 조사를 위해 **세 개의 서로 다른 AI CLI**
(Codex, Claude Code, agy/Antigravity)를 사람이 각각 별도 터미널에서 조작하며 사용합니다.
세 AI는 실시간으로 대화하지 않습니다 — 대신 아래 절차와 `coordination/` 폴더의 공유 이벤트
로그로 조율합니다. **작업을 시작하기 전에 반드시 이 문서 전체를 읽으세요.**

## 왜 이런 구조인가

세 AI가 자유롭게 계속 대화하며 조사하면 중복은 줄지만 토큰(비용)이 크게 늘어납니다.
반대로 전혀 조율하지 않으면 같은 회사/같은 사례를 중복 조사하게 됩니다.
그래서 "상시 대화" 대신 **공유 작업대장(이벤트 로그) + 선택적 토론**으로 갑니다.

## 작업 절차 (반드시 순서대로)

1. **저장소 최신화**: `git pull --rebase origin main`
2. **중복 검사**: 조사하려는 (회사, 업무영역, 사례)를 아래로 확인
   ```
   python coordination/check_duplicate.py --company "<회사명>" --area "<업무영역>" --case "<구체적 사례>"
   ```
   - "중복 가능성 높음"이 뜨면 다른 후보로 바꾸거나, 정말 다른 각도인지 재확인
   - 같은 회사라도 업무영역/사례가 다르면 중복이 아닙니다 (예: 영업 Copilot vs 재무 자동화)
3. **예약**: 중복이 아니면 바로 예약 (예약 즉시 commit+push되어 다른 AI에게 보임)
   ```
   python coordination/reserve.py --owner <claude|codex|agy> --company "<회사명>" \
       --area "<업무영역>" --case "<사례>" [--alias <다른표기>] [--url <참고url>]
   ```
4. **조사 수행**: 실제 리서치. 결과는 `findings/<owner>/<id>.md`에 저장
   (id는 reserve.py가 출력해줌, 예: `findings/claude/HYUNDAI-STEEL-SAIP.md`)
   - 기존 문서 형식(`benchmarks/2026-08-07_ai-productivity-benchmarking.md`)의 표 형식과
     "출처 신뢰도 A/B/C" 필드를 그대로 따를 것
5. **완료 처리**:
   ```
   python coordination/complete.py --id <id> --file findings/<owner>/<id>.md \
       --grade A|B|C --url <출처url> --owner <claude|codex|agy>
   ```
   - 출처 등급 C는 자동으로 토론 대상으로 등록됩니다

## 선택적 토론이 필요한 경우 (이 조건에 해당할 때만)

- 출처 등급이 C (홍보성 자료뿐, 1차 출처 없음)
- 정량 수치의 원인이 불명확함 (생성AI만의 효과인지, 기존 자동화·디지털화 효과와 섞여 있는지)
- 세아제강 관리부문/사무직과의 관련성이 논쟁적임 (현장/엔지니어링 성격이 강한 경우 등)
- 같은 사례를 다른 AI가 조사했는데 결론(AI Level, 관련성 등)이 크게 다름
- 12개사 Deep Dive 우선순위처럼 **사실검증이 아니라 방향성 판단**이 필요한 경우
  (이 경우 flag_debate.py의 --reason에 "우선순위 판단"이라고 명시해서 사실검증형과 구분할 것)

토론 시작:
```
python coordination/flag_debate.py --id <id> --by <claude|codex|agy> \
    --reason "<트리거 사유>" --claim "<구체적 주장, 1~2줄>"
```

## 판정 (Verdict) 규칙

- **판정은 그 건에 참여하지 않은 제3의 AI만** 할 수 있습니다 (원 조사자, 이의제기자 모두 제외)
  - verdict.py가 이를 강제로 검사하며, 관련자가 판정하려 하면 에러로 막습니다
- decision은 4가지: `adopt`(채택) / `hold`(보류, 추가확인 필요) / `exclude`(제외) / `needs_more_research`(재조사)
```
python coordination/verdict.py --id <id> --judge <claude|codex|agy> \
    --decision adopt|hold|exclude|needs_more_research --reasoning "<판정 근거 1~2줄>"
```
- **AI 셋의 판정만으로 최종 확정되지 않습니다.** `adopt` 판정이 나도 임원 보고 반영 여부는
  **이상민 과장님의 최종 확인**을 거쳐야 합니다. 이는 절차를 건너뛸 수 없는 규칙입니다.

## 원문 대화를 통째로 남기지 않기

토론이 끝나면 남기는 것은 **주장 - 반론 - 판정 - 근거 1~2줄**뿐입니다. 전체 대화 과정은
저장하지 않습니다 (저장 공간과 가독성을 위해). `coordination/events.jsonl`이 이 구조화된
기록의 원본이며, `python coordination/status.py`로 사람이 읽기 좋게 조회할 수 있습니다.

## 명령어 요약

| 상황 | 명령 |
|---|---|
| 뭘 조사할지 정하기 전 | `python coordination/status.py --queue` |
| 조사 시작 전 중복 확인 | `python coordination/check_duplicate.py ...` |
| 조사 항목 예약 | `python coordination/reserve.py ...` |
| 조사 완료 등록 | `python coordination/complete.py ...` |
| 다른 AI 결과에 이의 제기 | `python coordination/flag_debate.py ...` |
| 판정 대기 중인 토론 확인 | `python coordination/status.py --debates` |
| 토론 판정 | `python coordination/verdict.py ...` |
| 사람 승인 대기 목록 | `python coordination/status.py --pending-human` |

## 폴더 구조

```
ai-work-knowledge/
├── AGENTS.md                          # 이 문서 (Codex 등이 자동 인식)
├── CLAUDE.md                          # Claude Code용 (이 문서를 가리킴)
├── benchmarks/                        # 프로토콜 도입 이전 자료 (레거시, 참고용)
│   ├── 2026-08-07_ai-productivity-benchmarking.md   # 원본 40개사 Long List
│   └── claude/2026-08-07_new-cases-batch1.md        # Claude가 프로토콜 이전에 추가한 8개사
├── coordination/
│   ├── events.jsonl        # append-only 이벤트 로그 (모든 상태의 원본)
│   ├── lib.py               # 공통 로직 (의존성 없음, 표준 라이브러리만 사용)
│   ├── check_duplicate.py
│   ├── reserve.py
│   ├── complete.py
│   ├── flag_debate.py
│   └── verdict.py
├── findings/<owner>/<id>.md            # 프로토콜 도입 이후 개별 조사 결과 (owner = claude/codex/agy)
└── coordination/status.py 로 조회 (별도 report 파일 없음, 항상 최신 events.jsonl 기준)
```

## 알려진 한계

- 세 AI가 정확히 같은 순간에 push하면 git이 충돌할 수 있습니다. 스크립트가 `pull --rebase` 후
  재시도하지만, 실패하면 콘솔에 안내가 뜨니 사람이 `git status`로 확인해주세요.
- 회사명 중복 판정은 완전 자동이 아니라 토큰 유사도 기반 휴리스틱입니다. "중복 아님"이라고
  나와도 애매하면 한 번 더 사람 눈으로 확인하는 게 안전합니다.
