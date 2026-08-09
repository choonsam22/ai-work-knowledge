# Fujitsu — Kozuchi AI Agent, 영업 제안서 자동생성

> 조사자: Claude | 작성일: 2026-08-10 | 출처 신뢰도: A (Microsoft 공식 고객 사례)
> 상위 맥락: "12개사 우선 Deep Dive" #9 (영업 제안 Agent)

## 사례

Fujitsu 영업 조직은 방대한 제품 포트폴리오와 사내 곳곳에 흩어진 전문지식 때문에, 특히 신입
영업사원이 제안서를 작성하는 데 반복적·수작업적 시간을 과도하게 썼다. Azure AI Foundry의
Azure AI Agent Service 위에 자체 "Fujitsu Kozuchi Composite AI"(Semantic Kernel 기반
멀티에이전트 오케스트레이션)를 구축해, 여러 전문 Agent가 사내 분산 지식을 검색·종합해
**고객 맞춤 제안서를 데이터 기반으로 자동 생성**하도록 했다. 이 Agent는 제안서 생성뿐 아니라
신입사원에게 제품정보·전략 가이드를 제공하는 지식 검색 시스템 역할도 겸한다.

## 정량 효과

- 영업 생산성 **67% 향상**
- 적용 대상 3.5만 명 이상 직원 (전사 영업조직 규모)

## 세아제강 관리부문 관점

- 원 문서 후보 업무 Pool "영업 – 견적/제안자료 작성"과 정확히 대응하며, 5개 조사 대상 중
  **가장 구체적이고 높은 정량 수치(67%)**를 제시한 사례 중 하나
- 다만 Fujitsu는 자체 개발력(Kozuchi Composite AI, Semantic Kernel 오케스트레이션)을 보유한
  IT 기업이라는 점에서 세아제강이 그대로 이식하기보다는, "제안서 초안 자동생성 + 사내 지식
  검색" 기능만 상용 도구(Copilot Studio 등)로 축소 구현하는 것이 현실적

## 출처

- [Fujitsu is revolutionizing sales efficiency with Azure AI Agent Service (Microsoft 공식 고객 사례)](https://www.microsoft.com/en/customers/story/21885-fujitsu-azure-ai-foundry)
- [Customer Case Study: Fujitsu Kozuchi AI Agent Powered by Semantic Kernel (Microsoft Semantic Kernel 공식 블로그)](https://devblogs.microsoft.com/semantic-kernel/customer-case-study-fujitsu-kozuchi-ai-agent-powered-by-semantic-kernel/)
