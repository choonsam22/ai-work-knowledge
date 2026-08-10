# Willmott Dixon — Financial Reconciliation Agent

- 업무영역: 재무회계 / 계정조정 / 결산보고
- 기술: Dynamics 365 Finance, Microsoft Excel Financial Reconciliation Agent
- 출처 등급: B (Microsoft 공식 고객사례, 정량성과 미공개)
- 1차 출처: https://www.microsoft.com/en/customers/story/24555-willmott-dixon-dynamics-365-finance

## 확인된 사실

Willmott Dixon은 Dynamics 365 Finance 기반 재무환경에서 Excel의 Financial Reconciliation Agent를 사용한다. 에이전트는 조정 규칙을 적용하고 결과를 종합 보고서와 생성형 요약으로 제시한다. 재무책임자가 추가 기능의 유용성을 공식 사례에서 확인했다.

## 성과 해석

정량 절감시간이나 정확도는 공개되지 않았다. 따라서 ‘검증된 생산성 개선’ 사례보다, 계정조정의 규칙기반 판정과 생성형 설명을 결합한 참조 아키텍처로 보는 것이 타당하다.

## 작동 전제와 통제

조정 규칙은 LLM이 임의 생성하는 것이 아니라 회계정책과 계정별 허용오차에 따라 버전관리해야 한다. 생성형 요약에는 원거래와 근거 링크가 붙어야 하며, 전표 수정·상계는 승인 분리 원칙을 유지해야 한다.

## 공개되지 않은 것

적용 계정 수, 거래량, 자동조정률, 오매칭률, 마감기간 단축, 투자비는 공개되지 않았다.
