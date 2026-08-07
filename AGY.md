# 🌌 Antigravity/Gemini (agy) 작업 지침서

이 파일은 **Gemini (Antigravity/agy CLI)** 에이전트가 이 저장소를 열거나 작업을 시작할 때 우선적으로 참조하여, 기존 협업 기억과 실행 프로토콜을 즉시 상기(Restore Memory)하도록 유도하기 위한 지침서입니다.

---

## 🛡️ [핵심] 작업 절차 준수 요건

작업 시작 전, 반드시 저장소 루트의 **[AGENTS.md](file:///C:/Users/SeAH/ai-work-knowledge/AGENTS.md)**에 명시된 3대 AI(Codex, Claude, agy) 조율 프로토콜을 숙지하십시오.

1. **저장소 최신화:** `git pull --rebase origin main` (항상 가장 먼저 실행하여 타 AI의 작업 선점 현황 동기화)
2. **중복 검사:**
   ```powershell
   $env:PYTHONIOENCODING="utf-8"
   python coordination/check_duplicate.py --company "<회사명>" --area "<업무영역>" --case "<구체적 사례>"
   ```
3. **선점 예약 (즉시 push됨):**
   ```powershell
   $env:PYTHONIOENCODING="utf-8"
   python coordination/reserve.py --owner agy --company "<회사명>" --area "<업무영역>" --case "<사례>"
   ```
4. **리서치 및 보고서 작성:** 결과물은 반드시 `findings/agy/<ID>.md`에 저장
5. **완료 등록 및 원격 공유:**
   ```powershell
   $env:PYTHONIOENCODING="utf-8"
   python coordination/complete.py --id <ID> --file findings/agy/<ID>.md --grade A|B|C --url <참고URL> --owner agy
   ```

---

## ⚠️ 윈도우 터미널(cp949) 디코딩 장애 우회 방안
이 저장소는 한국어 Windows(MS Powershell) 환경에서 실행되므로, 파이썬이 CLI 출력을 긁어올 때 유니코드 문자로 인해 `cp949` 디코딩 에러가 발생할 수 있습니다. 
따라서 `coordination/` 아래의 스크립트 실행 시에는 **반드시 앞에 `$env:PYTHONIOENCODING="utf-8"` 환경변수를 함께 인입**하십시오.
* *예시:* `$env:PYTHONIOENCODING="utf-8"; python coordination/status.py --queue`

---

## 🎯 검증 3대 철칙 (Reality Check)
절대 화려한 솔루션사 마케팅 수치와 보도자료를 피상적으로 요약하고 끝내지 마십시오.
* **데이터 현실성:** 데이터 수집 정제(Data Cleansing)와 인프라 단일화에 수억 원이 선행 투자되어야 하는가?
* **사용성 이탈:** 챗봇 UI로 인한 입력 피로가 없는가? 비침습적 임베디드(Non-intrusive Widget) 방식인가?
* **정밀도 한계:** 환각(Hallucination)으로 인해 재무/법무 배임 리스크가 도사리고 있지 않은가?
보고서에는 반드시 위 맹점들을 날카롭게 해부하여 기각하고, **세아제강 관점의 현실적인 하이브리드 우회 대안**을 담아야 합니다.
