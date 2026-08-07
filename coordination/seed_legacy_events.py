#!/usr/bin/env python3
"""
프로토콜 도입 이전(benchmarks/ 폴더)에 이미 조사된 48개사를 이벤트 로그에 역등록.
한 번만 실행하는 마이그레이션 스크립트. owner="legacy" (실제 조사자가 claude/gpt 중
누구인지 커밋 기록상 구분 불가하므로 legacy로 통일).

목적: 이후 check_duplicate.py가 이 48개사를 "이미 조사됨"으로 인식하게 하기 위함.
정밀도보다 커버리지 우선 - area는 비워두고 use_case에 원문의 Benchmark Point를 그대로 넣음.
한글 사명으로 재검색될 가능성이 있는 곳은 aliases에 한글 표기를 넣어둠 (완전하지 않음,
새로 알게 된 별칭은 그때그때 append_event로 보강해도 됨).
"""
import sys
from pathlib import Path
from typing import NamedTuple, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import append_event, slugify_id  # noqa: E402


class LegacyEntry(NamedTuple):
    company: str
    use_case: str
    source_grade: Optional[str]
    aliases: list
    source_file: str


LEGACY_ORIGINAL_FILE = "benchmarks/2026-08-07_ai-productivity-benchmarking.md"
LEGACY_BATCH1_FILE = "benchmarks/claude/2026-08-07_new-cases-batch1.md"

LEGACY_ORIGINAL = [
    LegacyEntry("Tata Steel", "HR 문의, Invoice, 세금분류, 계약분석, 시장정보 등 전문 AI Agent 확대", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Nippon Steel", "전사 Copilot, 회의·메일·사내문서 검색 등 대규모 사무생산성 향상", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("POSCO", "인사·노무·행정·법무 경영지원 GPT, 업무시스템 처리로 확장", None, ["포스코"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("POSCO Group", "그룹 공통 AI(P-GPT), 보고서·분석·지식검색 및 직원 제작 Agent 확산", None, ["포스코그룹", "포스코 그룹", "P-GPT"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("JFE Shoji", "문서작성·정보정리·번역·Excel 등 관리업무 생성AI 활용", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Tata Steel TDA", "외부 뉴스·지정학·Commodity·내부 재무/운영정보 결합 분석", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Panasonic Connect", "전 직원 ConnectAI, AI 절감시간 정량화, 전사 확산", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Panasonic Connect", "AI에게 묻기->맡기기, 경리·법무·마케팅 Agent", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("DENSO", "관리·기술직 생성AI 대중화", None, ["덴소"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Toyota", "Office Productivity, 지식전승, 고객관계 등 전사 AI 프로그램", None, ["도요타"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Hyundai Mobis", "기술문서·논문·설계자료 요약·분석 등 사무/R&D 업무 지원", None, ["현대모비스"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Toshiba", "전사 Copilot, 개인 생산성에서 부서 프로세스 개선으로 확대", None, ["도시바"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Fujitsu", "분산 정보 검색 및 영업제안서 작성 Agent", None, ["후지쯔"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Hitachi", "개발·사무직 Copilot 활용", None, ["히타치"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Bosch", "전사 Ask Bosch 및 공급망/구매 영역 AI 활용", None, ["보쉬"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("tesa", "Supply Risk Agent, 공급망 위험 상시 감지·알림", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Schneider Electric", "이메일/회의 내용을 활용한 CRM 정보 업데이트 자동화", None, ["슈나이더 일렉트릭"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Dow", "Freight Rate·Invoice·계약운임 자동 비교 및 과다청구 탐지", None, ["다우"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Eaton", "SOP 작성 등 반복 문서업무 단축", None, ["이튼"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Regal Rexnord", "Employee Agent를 통한 사내 문의 처리", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Chin Hin Group", "구매 비교, 재무/Board Reporting, 제안·보고 업무", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Bayer", "전사적으로 대규모 생성AI Use Case 발굴", None, ["바이엘"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Eastman Chemical", "CRM 내 고객·영업정보·Spreadsheet·Call Summary 통합 Insight", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("TotalEnergies", "BuyerCompanion: 요구사항->공급사->계약 확인->구매추천", None, ["토탈에너지스"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Tüpraş", "구매 계약서·법적 요구사항·Supplier Communication 지원", None, ["튀프라쉬"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("HELLENiQ Energy", "정보검색·회의·이메일 등 전사 사무생산성 향상", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("JCB", "일상업무->내부 전문업무->고객서비스 단계적 AI 활용", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("NYK", "회의록·번역·시장조사에서 AI Agent 및 그룹 확산으로 확대", None, ["일본우선"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("NTT Docomo", "대규모 전사 배포, 생산성 KPI를 월 시간 단위로 설정", None, ["도코모"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Sumitomo Corp", "생성AI를 전화·PC와 같은 업무 인프라로 정의", None, ["스미토모"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("KT", "흩어진 사내 파일의 통합 검색·요약", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("SCSK", "현업이 Agent 후보를 제안하고 선별 개발하는 운영모델", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("BCI", "내부감사 보고서 및 대규모 Survey 분석", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("DLA Piper", "법무 문서 생성·데이터 분석 등 운영업무", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Verdantas", "Workday·재무·ERP·ServiceNow·파일을 Agent로 통합 검색", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("ICG", "영업제안, 채용 Onboarding, 재무분석", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Coca-Cola Andina", "개인별 인사·복리후생 HR Agent", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Estée Lauder", "소비자/시장 Insight 수집·분석", None, ["에스티 로더"], LEGACY_ORIGINAL_FILE),
    LegacyEntry("XP Inc.", "내부감사 생산성 향상", None, [], LEGACY_ORIGINAL_FILE),
    LegacyEntry("Capita", "전사 Copilot/Agent 기반 업무시간 절감", None, [], LEGACY_ORIGINAL_FILE),
]

LEGACY_CLAUDE_BATCH1 = [
    LegacyEntry("ABB Group", "Genix Copilot - 탄소배출·설비상태 자연어 질의응답, O&M비용 40%↓", "B", ["ABB"], LEGACY_BATCH1_FILE),
    LegacyEntry("Sandvik", "Manufacturing Copilot - 제품문서·품질기록 자연어 검색, 생산성 30%↑", "B", [], LEGACY_BATCH1_FILE),
    LegacyEntry("Rio Tinto", "재무부서 Copilot Studio + Power BI Copilot 도입", "C", ["리오틴토"], LEGACY_BATCH1_FILE),
    LegacyEntry("Campari Group", "M365 Copilot + Viva - 이메일/회의 준비 등 일반 사무업무, 주2h 절감", "B", ["캄파리"], LEGACY_BATCH1_FILE),
    LegacyEntry("thyssenkrupp Schulte", "Dynamics 365 Sales + M365 Copilot 영업 생산성", "B", ["티센크루프 슐테"], LEGACY_BATCH1_FILE),
    LegacyEntry("thyssenkrupp Automation Engineering", "Siemens Industrial Copilot 엔지니어링 설계 보조", "B", ["티센크루프"], LEGACY_BATCH1_FILE),
    LegacyEntry("Hyundai Steel", "S2W SAIP 생성AI 플랫폼 - 경영지원 챗봇", "C", ["현대제철"], LEGACY_BATCH1_FILE),
    LegacyEntry("China Baowu", "철강 특화 LLM xIn3Plat - 조업 의사결정 지원", "C", ["바오우", "중국보무", "Baowu"], LEGACY_BATCH1_FILE),
]


def seed() -> None:
    count = 0
    for entry in LEGACY_ORIGINAL + LEGACY_CLAUDE_BATCH1:
        tid = slugify_id(entry.company, entry.use_case[:20])
        append_event({
            "type": "RESERVE",
            "id": tid,
            "owner": "legacy",
            "company": entry.company,
            "aliases": entry.aliases,
            "work_area": "",
            "use_case": entry.use_case,
            "source_urls": [],
        })
        append_event({
            "type": "COMPLETE",
            "id": tid,
            "status": "done",
            "file": entry.source_file,
            "source_grade": entry.source_grade,
            "source_urls": [],
        })
        count += 1
    print(f"[시딩 완료] {count}건 등록")


if __name__ == "__main__":
    seed()
