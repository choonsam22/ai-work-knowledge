# 신규 벤치마킹 사례 Batch 1 (Claude 조사)

> 작성일: 2026-08-07
> 조사자: Claude
> 목적: 기존 `benchmarks/2026-08-07_ai-productivity-benchmarking.md`의 40개사 Long List와 겹치지 않는 신규 벤치마킹 사례 확보
> 중복 확인: 기존 문서의 40개사(Tata Steel, Nippon Steel, POSCO, JFE Shoji, Panasonic Connect, DENSO, Toyota, Hyundai Mobis, Toshiba, Fujitsu, Hitachi, Bosch, tesa, Schneider Electric, Dow, Eaton, Regal Rexnord, Chin Hin, Bayer, Eastman Chemical, TotalEnergies, Tüpraş, HELLENiQ Energy, JCB, NYK, NTT Docomo, Sumitomo, KT, SCSK, BCI, DLA Piper, Verdantas, ICG, Coca-Cola Andina, Estée Lauder, XP Inc., Capita)와 아래 8개사는 중복되지 않음

---

## F. 산업재·중공업·소재 (신규)

| # | 기업 | 산업 | 주요 관리영역 / Benchmark Point | 임시 Level | 출처 등급 |
|---:|---|---|---|---|---|
| 41 | ABB Group | 전기·자동화 | Genix Copilot(Azure OpenAI 기반) — 탄소배출·설비상태 자연어 질의응답, O&M 비용 40%↓, 생산효율 30%↑, 서비스콜 80%↓ | L2→L4 | A/B |
| 42 | Sandvik | 기계·엔지니어링 | Manufacturing Copilot(Azure OpenAI+AI Search) — 제품문서·품질기록 자연어 검색, 문제해결 속도 및 생산성 최대 30%↑ | L1→L2 | A/B |
| 43 | Rio Tinto | 광업 | 재무부서에 Copilot Studio + Power BI Copilot 도입, 자연어 질의로 데이터 분석·요약 시간 단축 | L1→L2 | C |
| 44 | Campari Group | 소비재(주류) | M365 Copilot + Viva — 이메일/회의 준비 등 일반 사무업무, 주당 2시간 절감, 생산성 81%↑ 응답, 마케팅 카피 비용 18%↓ | L1 | A/B |
| 45 | thyssenkrupp Schulte | 철강 유통 | Dynamics 365 Sales + M365 Copilot — 영업사원 반복업무 절감, 고객 응대 시간 확보 | L1→L3 | A/B |
| 46 | thyssenkrupp Automation Engineering (Siemens Industrial Copilot) | 산업 자동화 | Azure OpenAI 기반 엔지니어링 Copilot — 패널 시각화 30초 생성, 코드 생성 후 20%만 수정 필요 | L2→L3 | A/B |
| 47 | Hyundai Steel | 철강(국내) | S2W 'SAIP' 생성AI 플랫폼 — 철강 특화 빅데이터 기반 경영지원 챗봇, 업무 효율화 | L1→L2 | C |
| 48 | China Baowu | 철강 | 자체 개발 철강 특화 LLM 'xIn³Plat'(기반모델·산업버티컬모델·업무시나리오모델 3계층) — 전로 조업·냉연 공정 의사결정 지원, 안전·효율 개선 | L2→L4 | C |

---

## 상세 메모

### ABB Group — Genix Copilot
- Azure OpenAI Service 기반, 기존 Genix 산업 IoT/분석 스위트에 통합
- 예시 질의: "전 공장의 탄소배출 현황은?" → Copilot이 배출 한도 임박 공장을 식별하고 대응 방안 제시
- Level 근거: 단순 검색을 넘어 이상 탐지 후 액션 권고까지 하므로 L4(Agentic)에 근접
- 출처: [ABB embraces Azure OpenAI Service | Microsoft Customer Stories](https://www.microsoft.com/en/customers/story/19773-abb-group-azure) / [ABB Genix Copilot 발표](https://new.abb.com/news/detail/122021/helping-industries-do-better-with-generative-ai-abb-launches-genix-copilot-with-microsoft)

### Sandvik — Manufacturing Copilot
- Cimatron, GibbsCAM, SigmaNEST 등 CAD/CAM 제품에 탑재, 40만 사용자 대상 확산 예정
- 브랜드별 고유 지식(제품문서·품질기록·영상)으로 학습된 Shared Service 구조
- 출처: [Sandvik revolutionizes manufacturing with Microsoft AI solutions](https://www.microsoft.com/en/customers/story/22965-sandvik-azure-open-ai-service)

### Rio Tinto — 재무부서 Copilot
- 재무 담당자가 Power BI 내 Copilot으로 데이터 분석·요약 — 기존 수시간 걸리던 작업 단축
- 세아제강 "재무·회계 – 실적/계획 차이 분석" 후보 업무와 직접 대응
- 출처: [Rio Tinto brings automation, Copilot to its finance function - iTnews](https://www.itnews.com.au/news/rio-tinto-brings-automation-copilot-to-its-finance-function-625319)

### Campari Group — M365 Copilot + Viva
- 일반 사무 생산성(이메일, 회의 준비/요약) 중심으로 세아제강 L1 사례와 가장 유사
- 정량 효과: 주당 2시간 절감, 81% 생산성 향상 응답, 86% 업무품질 향상 응답
- 출처: [Campari Group enhances collaboration and creativity with M365 Copilot and Viva](https://www.microsoft.com/en/customers/story/19797-campari-microsoft-viva)

### thyssenkrupp Schulte / thyssenkrupp Automation Engineering
- Schulte(유통 자회사): 영업 Copilot → 세아제강 "영업 – 고객문의 대응/제안자료 작성"과 유사
- Automation Engineering: Siemens Industrial Copilot(Azure OpenAI) → 엔지니어링 설계 보조, 관리부문보다는 기술부서에 가까우나 "반복 설계업무 자동화" 관점에서 참고 가능
- 출처: [thyssenkrupp Schulte | Microsoft Customer Stories](https://www.microsoft.com/en/customers/story/18919-thyssenkrupp-schulte-dynamics-365-sales), [Siemens and Microsoft scale industrial AI](https://news.microsoft.com/source/2024/10/24/siemens-and-microsoft-scale-industrial-ai/)

### Hyundai Steel — SAIP
- 국내 철강사 사례로 세아제강과 산업·시장 맥락이 가장 유사 → 우선 Deep Dive 후보로 추천
- 출처: [S2W Provides Generative AI Platform 'SAIP' to Hyundai Steel - PR Newswire](https://www.prnewswire.com/news-releases/s2w-provides-generative-ai-platform-saip-to-hyundai-steel-302149971.html) (C등급, 1차 확인 필요)

### China Baowu — xIn³Plat
- 조업 현장(전로 조업자, 냉연 오퍼레이터) 대상이라 순수 "관리부문"보다는 현장 관리자 지원에 가까움 — 관리부문 관점보다 참고용으로 분류
- 출처: 뉴스 기사 기반(C등급), 공식 발표 원문 추가 확인 필요

---

## 다음 조사 후보 (미확인, 추가 검증 필요)
- BASF / Evonik / Covestro — 검색 결과 공식 사례 미확인, 재검색 필요
- POSCO Holdings (지주) — 기존 문서는 POSCO/POSCO Group만 포함, 지주 차원 별도 사례 있는지 확인 필요
- JSW Steel, Gerdau, Severstal, SSAB — 생성AI 관리업무 관련 공식 사례 미확인 (production/AI 사례는 있으나 관리부문향 아님)
