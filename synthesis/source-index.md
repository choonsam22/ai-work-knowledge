# 전체 출처 색인 (Source Index)

> 이 문서는 `report-draft.md`(서사형 보고서)의 근거 자료를 빠짐없이, 정확하게 추적하기 위한
> 색인이다. 조사된 모든 자료를 포함한다 — 등급이 낮거나(C) 본문에서 제외된 사례도 예외 없이
> 여기 실려 있으며, 출처 링크가 없는 경우 "링크 미수집"이라고 명시했지 임의로 추정하지 않았다.
> 작성: Claude · 2026-08-10

---

## A. 심층조사 완료 — 25건 (정밀 출처 확보)

### A-1. Tata Steel (5건 + Gemini 종합비평 1건)

공통 배경: Google Cloud와 협력해 전사 Agentic AI 전략(300개 이상 전문 Agent, 9개월 내 배포)을
발표. 아래 5건은 이 전략을 Use Case 단위로 분해한 것이다.

| Use Case | 핵심내용 | 정량효과 | 등급 | 조사자 |
|---|---|---|---|---|
| HR 문의 대응 (TDA) | 사내 HR 헬프데스크 역할을 수행하는 Digital Assistant | 반복 직원 티켓 70%+ 자율 해결 | A | Claude |
| Invoice·GST 세금분류 | Invoice 처리와 세금분류를 자동화하는 Agent | 정성 효과 위주, 수치 비공개 | A | Claude |
| 계약분석 (Contract Analysis) | 계약 조항의 리스크를 분석하는 Agent | 정성 효과 위주 | B | Claude |
| 불만데이터 분석·라우팅 | 고객 불만 데이터를 분석해 담당 부서로 라우팅 | 정성 효과 위주 | A | Claude |
| ZEN AI 로우코드 플랫폼 | 현업 직원이 로우코드로 직접 Agent 제작 | 9개월 내 300개+ Agent 배포 | A | Claude |

- 1차 출처: [Tata Steel Partners with Google Cloud To Deploy a Unified Agentic AI Across its Global Value Chain (공식 뉴스룸)](https://www.tatasteel.com/newsroom/press-releases/india/2026/tata-steel-partners-with-google-cloud-to-deploy-a-unified-agentic-ai-across-its-global-value-chain/)
- 동일 발표 미러: [Google Cloud Press Corner](https://www.googlecloudpresscorner.com/2026-04-22-Tata-Steel-Partners-with-Google-Cloud-To-Deploy-a-Unified-Agentic-AI-Across-its-Global-Value-Chain)
- **Gemini 종합비평** (`benchmarks/gemini/deep_dive_reports/01_tata_steel_agentic_ai.md`): "300개 Agent"의 상당수가 자율집행형(L3~L4)이 아닌 단순 검색 챗봇(L2) 수준일 가능성, RBAC 권한 붕괴 위험, 토큰 비용 통제 부재를 지적. 대안으로 "소수 고가치 공통 Agent 5종을 중앙에서 정교하게 튜닝"하는 모델 제안.

### A-2. POSCO — 경영지원 GPT

- 핵심내용: 사내 폐쇄형 LLM 'P-GPT'를 인사·세무·법무 시스템과 연계, 37개 그룹사·2만여 명 대상 서비스
- 정량효과: 37개사·2만여 명 (발표 수치)
- 등급: B (조사자 Gemini/agy가 자체적으로 Reality Check 포함해 작성)
- **Gemini 비평 요지**: 사내 폐쇄형 sLLM은 GPT-4o급 대비 추론력이 떨어져 이를 보완하려면 GPU 서버(H100급)에 수십억 원대 투자가 지속 필요함. 세무·법무 영역의 환각(hallucination) 리스크가 배임으로 이어질 수 있음. 지식그래프 구축은 사실상 수작업 라벨링. 대안으로 "퍼블릭 엔터프라이즈 API + 담당자 전용 초안 어시스턴트(비침습형)" 제안.
- 출처: [포스코, 경영지원 GPT 전면 오픈…AI 기반 스마트워크 시대 '성큼' (포스코그룹 공식 뉴스룸)](https://newsroom.posco.com/kr/%ED%8F%AC%EC%8A%A4%EC%BD%94-%EA%B2%BD%EC%98%81%EC%A7%80%EC%9B%90-gpt-%EC%A0%84%EB%A9%B4-%EC%98%A4%ED%94%88ai-%EA%B8%B0%EB%B0%98-%EC%8A%A4%EB%A7%88%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%8B%9C/), [포스코 공식 보도자료 페이지](https://www.posco.co.kr/homepage/docs/kor7/jsp/prcenter/press/s91c600110v.jsp?onPage=1&idx=2593)

### A-3. LG전자 — LGenie 전사 AI 에이전트 플랫폼

- 핵심내용: 사내 챗봇 LGenie를 EXAONE 기반 + Azure/ChatGPT/Gemini 결합 전사 에이전트 플랫폼으로 고도화 중 (개발·영업·SCM·구매·마케팅)
- 정량효과: 향후 2~3년 내 전사 생산성 **30% 향상 목표** (실측 아님 — Codex가 명시적으로 "목표치, 인과적 성과 아님" 경고)
- 등급: A (공식 발표이나 목표치)
- 조사자: Codex
- 출처: [LG Electronics CEO Sets Strategic Direction for Profit-Driven Growth (공식 뉴스룸, 2026-01-08)](https://www.lg.com/global/newsroom/news/corporate/lg-electronics-ceo-sets-strategic-direction-for-profit-driven-growth-prioritizing-speed-and-action/), [DX for the Company: Innovation in the Way You Work](https://www.lg.com/global/newsroom/lg-story/beyond-news/dx-for-the-company-innovation-in-the-way-you-work/)

### A-4. 12개사 우선 Deep Dive 중 나머지 6건 (Claude 신규 조사, 2026-08-10)

| 기업 | 핵심내용 | 정량효과 | 등급 | 출처 |
|---|---|---|---|---|
| Nippon Steel | M365 Copilot 단계적 전사 확산 (300→4,400→11,000석), 챔피언 제도 | 월 AI회의메모 2만건·메일요약 4,500건, 연간 수만시간 절감(전망) | A | [Microsoft 고객사례](https://www.microsoft.com/ja-jp/customers/story/23624-nippon-steel-corporation-microsoft-365-copilot) |
| Toshiba | Copilot 로그+Viva Insights 결합해 개인생산성→부서 프로세스 개선으로 승격 | 1인당 월 5.6시간 절감, 총무 설문분석 3개월→1일 | A | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/23123-toshiba-corporation-microsoft-viva-insights) |
| Schneider Electric | Copilot for Sales(CRM 자동화) + Industrial Copilot(엔지니어링, 별도) | 영업: 정성효과 위주 / 산업Copilot: 개발시간 30~50%↓ | B | [Sales 사례](https://www.microsoft.com/en/customers/story/18860-schneider-electric-microsoft-365-copilot-for-sales), [Industrial Copilot 발표](https://www.powersystemsdesign.com/articles/schneider-electric-unveils-industrial-gen-ai-copilot-in-collaboration-with-microsoft/97/22759) |
| Fujitsu | Kozuchi Composite AI(멀티에이전트)로 제안서 자동생성+신입 지식검색 | 영업 생산성 67%↑, 적용 3.5만명 | A | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/21885-fujitsu-azure-ai-foundry), [Semantic Kernel 블로그](https://devblogs.microsoft.com/semantic-kernel/customer-case-study-fujitsu-kozuchi-ai-agent-powered-by-semantic-kernel/) |
| DENSO | M365 Copilot 사무직 3만명 단계적 확산(300→6,000→30,000) | 1인당 월 12시간 절감, 2026.3 기준 이용률 99% | A | [Microsoft 고객사례](https://www.microsoft.com/ja-jp/customers/story/19426-denso-corporation-microsoft-365-copilot), [JBS 파트너사 보도](https://www.jbs.co.jp/news/2026/0312-2) |
| NTT Docomo | M365 Copilot 26,700 라이선스 전사배포, 사전 공통 KPI 설계 | 1인당 월 10시간 생산성 창출 KPI 달성, MAU 90% | A | [Microsoft 고객사례](https://www.microsoft.com/ja-jp/customers/story/26409-ntt-docomo-microsoft-365-e5) |

### A-5. Batch 1 — 신규 확보 8건 (Claude, 원 40개사 목록 외 추가, 2026-08-07)

| 기업 | 핵심내용 | 정량효과 | 등급 | 출처 |
|---|---|---|---|---|
| ABB Group | Genix Copilot(Azure OpenAI) — 탄소배출·설비상태 자연어 질의응답 | O&M 비용 40%↓, 생산효율 30%↑, 서비스콜 80%↓ | B | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/19773-abb-group-azure), [ABB 발표](https://new.abb.com/news/detail/122021/helping-industries-do-better-with-generative-ai-abb-launches-genix-copilot-with-microsoft) |
| Sandvik | Manufacturing Copilot(Azure OpenAI+AI Search) — 제품문서·품질기록 검색 | 문제해결 속도·생산성 최대 30%↑, 40만 사용자 대상 확산 예정 | B | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/22965-sandvik-azure-open-ai-service) |
| Rio Tinto | 재무부서 Copilot Studio + Power BI Copilot | 데이터 분석·요약 시간 단축 (구체적 수치 비공개) | C | [iTnews](https://www.itnews.com.au/news/rio-tinto-brings-automation-copilot-to-its-finance-function-625319) |
| Campari Group | M365 Copilot + Viva — 이메일/회의 준비 등 일반 사무업무 | 주당 2시간 절감, 생산성향상 응답 81%, 업무품질향상 응답 86% | B | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/19797-campari-microsoft-viva) |
| thyssenkrupp Schulte | Dynamics 365 Sales + M365 Copilot — 영업 반복업무 절감 | 정량수치 비공개 | B | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/18919-thyssenkrupp-schulte-dynamics-365-sales) |
| thyssenkrupp Automation Engineering | Siemens Industrial Copilot(Azure OpenAI) — 엔지니어링 설계 보조 | 패널 시각화 30초 생성, 코드 생성 후 20%만 수정 필요 | B | [Microsoft/Siemens 발표](https://news.microsoft.com/source/2024/10/24/siemens-and-microsoft-scale-industrial-ai/) |
| Hyundai Steel | S2W 'SAIP' 생성AI 플랫폼 — 철강 특화 경영지원 챗봇 | 업무 효율화 (구체적 수치 비공개) | C — 1차 확인 필요 | [PR Newswire](https://www.prnewswire.com/news-releases/s2w-provides-generative-ai-platform-saip-to-hyundai-steel-302149971.html) |
| China Baowu | 자체 개발 철강 특화 LLM 'xIn³Plat' (기반모델·산업버티컬모델·업무시나리오모델 3계층) | R&D 효율 30%↑ (언론 보도 기준) | C — 공식 발표 원문 미확인 | [Yicai Global](https://www.yicaiglobal.com/news/chinas-baowu-launches-self-developed-ai-tool-for-steel-industry) |

### A-6. Gemini 심층 비평 대상 4건 (Tata Steel 제외, 2026-08-07)

| 기업 | 핵심내용 (홍보자료 기준) | Gemini 비평 핵심 | 등급 | 출처 |
|---|---|---|---|---|
| Dow | Copilot Studio 에이전트로 일 4,000건 중 비정형 PDF 20%를 자동검증 | OCR·LLM 파싱 오류율, 오탐 알람 리스크. 대안: 대형 파트너사는 API/정형 템플릿 강제, PDF는 AI를 "추출"에만 한정 | B | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/19829-dow-microsoft-365-copilot) |
| TotalEnergies | 'BuyerCompanion' — 5만유로 이하 소액구매 자동 규격화+단가계약 자동체크, 조달비용 10%↓ | 챗봇 UI 자체에 대한 임직원 이탈·귀찮음. 대안: ERP 화면에 내장된 "조용한 팝업 위젯"형 UX | B | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/25505-totalenergies-agents) |
| tesa | 'Supply Risk Agent' — 뉴스·날씨 실시간 감시로 11개 공장 리스크 선제 알림 | 실시간 알림의 "늑대소년 신드롬"(알림 피로). 대안: 분기 단위 거시 리스크 요약 + 계약만기 6~9개월 전 사전 알림으로 전환 | B | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/25507-tesa-se-microsoft-copilot) |
| Panasonic Connect | 데이터 레이크하우스+LLM으로 1만건 계약·MSA 취합을 2주→2~3시간 단축 | 드라마틱한 성과 뒤에 숨은 거대한 선행 인프라(레이크하우스) 투자. 대안: 표준 엑셀 스키마 강제화 + 경량 Python 파이프라인 우선 | A | [Databricks 공식 고객사례](https://www.databricks.com/customers/panasonic/lakeflow-connect) (일반 AI 추진 맥락: [Panasonic 공식 발표](https://news.panasonic.com/jp/press/jn250707-2)) |

---

## B. 1차 스크리닝 롱리스트 — 40개사

> 원문: `benchmarks/2026-08-07_ai-productivity-benchmarking.md` 4장. 설명은 원문 표현을 그대로
> 유지했다. "심층조사 완료"로 표시된 12개사는 위 A절에 상세 출처가 있다. 나머지는 1차
> 스크리닝 단계에서 회사명·업무영역·Level만 기록했고, 개별 기사 링크는 수집하지 않았다 —
> 존재하지 않는 링크를 임의로 만들지 않고 "링크 미수집"으로 명시한다.

### B-1. 철강·소재

| # | 기업 | Benchmark Point | Level | 출처 상태 |
|---:|---|---|---|---|
| 1 | Tata Steel | HR 문의, Invoice, 세금분류, 계약분석, 시장정보 등 전문 AI Agent 확대 | L2→L4 | **심층조사 완료 (A-1 참고)** |
| 2 | Nippon Steel | 전사 Copilot, 회의·메일·사내문서 검색 등 대규모 사무생산성 향상 | L1→L2 | **심층조사 완료 (A-4 참고)** |
| 3 | POSCO | 인사·노무·행정·법무 경영지원 GPT, 업무시스템 처리로 확장 | L2→L3 | **심층조사 완료 (A-2 참고)** |
| 4 | POSCO Group / P-GPT | 그룹 공통 AI, 보고서·분석·지식검색 및 직원 제작 Agent 확산 | L1→L4 | A-2와 동일 발표 계열, 별도 링크 미수집 |
| 5 | JFE Shoji | 문서작성·정보정리·번역·Excel 등 관리업무 생성AI 활용 | L1 | [JFE 상사 지속가능경영 페이지](https://www.jfe-shoji.co.jp/sustainability/diversity/) |
| 6 | Tata Steel – TDA(시장정보) | 외부 뉴스·지정학·Commodity·내부 재무/운영정보 결합 분석 | L2→L4 | A-1과 별개 기능, 개별 링크 미수집 |

### B-2. 제조업·산업재

| # | 기업 | Benchmark Point | Level | 출처 상태 |
|---:|---|---|---|---|
| 7 | Panasonic Connect | 전 직원 ConnectAI, AI 절감시간 정량화, 전사 확산 | L1→L4 | **심층조사 완료 (A-6 참고)** |
| 8 | Panasonic Connect – 업무 Agent | 경리·법무·마케팅 Agent | L3→L4 | A-6과 동일 계열, 개별 링크 미수집 |
| 9 | DENSO | 관리·기술직 생성AI 대중화 | L1→L2 | **심층조사 완료 (A-4 참고)** |
| 10 | Toyota | Office Productivity, 지식전승, 고객관계 등 전사 AI 프로그램 | L1→L4 | [Toyota Global Newsroom](https://global.toyota/en/newsroom/corporate/42805724.html) |
| 11 | Hyundai Mobis | 기술문서·논문·설계자료 요약·분석 등 사무/R&D 업무 지원 | L1→L2 | 링크 미수집 |
| 12 | Toshiba | 전사 Copilot, 개인 생산성→부서 프로세스 개선 | L1→L3 | **심층조사 완료 (A-4 참고)** |
| 13 | Fujitsu | 분산 정보 검색 및 영업제안서 작성 Agent | L2→L4 | **심층조사 완료 (A-4 참고)** |
| 14 | Hitachi | 개발·사무직 Copilot 활용 | L1→L3 | 링크 미수집 |
| 15 | Bosch | 전사 Ask Bosch 및 공급망/구매 영역 AI 활용 | L2→L4 | 링크 미수집 |
| 16 | tesa | Supply Risk Agent, 공급망 위험 상시 감지·알림 | L4 | **심층조사 완료 (A-6 참고)** |
| 17 | Schneider Electric | 이메일/회의 내용을 활용한 CRM 정보 업데이트 자동화 | L3 | **심층조사 완료 (A-4 참고)** |
| 18 | Dow | Freight Rate·Invoice·계약운임 자동 비교 및 과다청구 탐지 | L3→L4 | **심층조사 완료 (A-6 참고)** |
| 19 | Eaton | SOP 작성 등 반복 문서업무 단축 | L1→L3 | 링크 미수집 |
| 20 | Regal Rexnord | Employee Agent를 통한 사내 문의 처리 | L2→L3 | 링크 미수집 |
| 21 | Chin Hin Group | 구매 비교, 재무/Board Reporting, 제안·보고 업무 | L1→L3 | 링크 미수집 |
| 22 | Bayer | 전사적으로 대규모 생성AI Use Case 발굴 | L1→L3 | 링크 미수집 |
| 23 | Eastman Chemical | CRM 내 고객·영업정보·Spreadsheet·Call Summary 통합 Insight | L2→L3 | 링크 미수집 |

### B-3. 에너지·중공업·저마진 산업

| # | 기업 | Benchmark Point | Level | 출처 상태 |
|---:|---|---|---|---|
| 24 | TotalEnergies | BuyerCompanion: 요구사항→공급사→계약 확인→구매추천 | L3→L4 | **심층조사 완료 (A-6 참고)** |
| 25 | Tüpraş | 구매 계약서·법적 요구사항·Supplier Communication 지원 | L2→L3 | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/23105-tupras-microsoft-365-copilot) |
| 26 | HELLENiQ Energy | 정보검색·회의·이메일 등 전사 사무생산성 향상 | L1→L3 | 링크 미수집 |
| 27 | JCB | 일상업무→내부 전문업무→고객서비스 단계적 AI 활용 | L1→L3 | 링크 미수집 |
| 28 | NYK / 일본우선 | 회의록·번역·시장조사에서 AI Agent 및 그룹 확산으로 확대 | L1→L3 | 링크 미수집 |

### B-4. 전사 확산/운영모델 Benchmark

| # | 기업 | Benchmark Point | Level | 출처 상태 |
|---:|---|---|---|---|
| 29 | NTT Docomo | 대규모 전사 배포, 생산성 KPI를 월 시간 단위로 설정 | L1→L3 | **심층조사 완료 (A-4 참고)** |
| 30 | Sumitomo Corp. | 생성AI를 전화·PC와 같은 업무 인프라로 정의 | L1→L3 | [Microsoft 고객사례](https://www.microsoft.com/en/customers/story/21914-sumitomo-corporation-microsoft-365-copilot) |
| 31 | KT | 흩어진 사내 파일의 통합 검색·요약 | L2 | 링크 미수집 |
| 32 | SCSK | 현업이 Agent 후보를 제안하고 선별 개발하는 운영모델 | L2→L4 | 링크 미수집 |

### B-5. 특정 관리업무 Benchmark

| # | 기업 | Benchmark Point | 출처 상태 |
|---:|---|---|---|
| 33 | BCI | 내부감사 보고서 및 대규모 Survey 분석 | 링크 미수집 |
| 34 | DLA Piper | 법무 문서 생성·데이터 분석 등 운영업무 | 링크 미수집 |
| 35 | Verdantas | Workday·재무·ERP·ServiceNow·파일을 Agent로 통합 검색 | 링크 미수집 |
| 36 | ICG | 영업제안, 채용 Onboarding, 재무분석 | 링크 미수집 |
| 37 | Coca-Cola Andina | 개인별 인사·복리후생 HR Agent | 링크 미수집 |
| 38 | Estée Lauder | 소비자/시장 Insight 수집·분석 | 링크 미수집 |
| 39 | XP Inc. | 내부감사 생산성 향상 | 링크 미수집 |
| 40 | Capita | 전사 Copilot/Agent 기반 업무시간 절감 | 링크 미수집 |

**요약**: 40개사 중 12개사는 심층조사(A절)로 이어져 정밀 출처가 있고, 5개사는 1차 스크리닝
단계에서 링크를 확보했으며(JFE Shoji, Toyota, Tüpraş, Sumitomo + POSCO/Tata Steel 관련
파생 2건), 나머지 23개사는 회사명·업무영역·Level만 기록되고 개별 출처 링크는 아직
수집되지 않았다. 이 23개사에 시간을 더 쓸지는 조사 범위 확대 여부에 달려 있다.

---

## C. 등급 기준 (참고)

- **A**: 기업 공식 발표, IR/Annual Report, 공식 Newsroom
- **B**: Microsoft/Google/Databricks 등 솔루션사 공식 고객사례 (고객 인터뷰 기반이나 홍보 목적 병존)
- **C**: 언론기사, 2차 자료, 공식 1차 확인 미완료

## D. 조사 참여 및 방법

- **Claude**: A-1(Tata Steel 5건 종합), A-4(6건 신규), A-5(Batch1 8건), 큐레이션 전체
- **Codex**: A-3(LG전자)
- **Gemini(agy)**: A-2(POSCO, 자체 Reality Check 포함), A-6(Dow/TotalEnergies/tesa/Panasonic Reality Check), A-1의 Gemini 종합비평
- 원본 데이터 저장소: [choonsam22/ai-work-knowledge](https://github.com/choonsam22/ai-work-knowledge) — `benchmarks/`, `findings/` 폴더
