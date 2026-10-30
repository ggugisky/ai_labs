---
id: ailabs:raw/2026-10-30-gtm-master-framework
type: Document
status: draft
created: 2026-10-30
area: ai-labs
relations:
  - type: discusses
    target: ailabs:organization/ai-labs
provenance:
  sources:
    - id: slack:F0CDLRJE2FN
      title: GTM_Master_Framework.pptx
      url: https://landmaster.slack.com/files/UBH3WR79R/F0CDLRJE2FN/gtm_master_framework.pptx
      accessed: 2026-10-30
      kind: Slack file
---

# GTM Master Framework 분석

## 문서 개요

`GTM_Master_Framework.pptx`는 앱 개발자의 디지털 제품 상용화를 제품 정의부터 출시 후 운영까지 8개 단계로 정리한 실무 가이드다. 게임의 성장 문법과 유틸리티 앱·SaaS의 마찰 없는 사용성을 구분하고, 제품·수익·마케팅·운영을 하나의 단위경제 모델로 연결한다. 본 문서는 원본 슬라이드 텍스트 기반 1차 분석이며 시장·스토어 정책·수수료·벤치마크는 별도 검증이 필요하다.

## 핵심 주장

1. GTM은 출시 직전 마케팅이 아니라 초기 제품·기술 설계부터 시작된다.
2. 핵심 루프와 UVP를 명확히 하고 다운로드 후 첫 가치 경험까지의 시간(TTV)을 줄여야 한다.
3. 수익화·분석·권한·개인정보 보호를 초기 SDK와 데이터 구조에 통합해야 한다.
4. 성장 예산은 LTV/CAC, CAC 회수 기간, 유지율과 연결하고 단위경제 검증 전 대규모 브랜드 마케팅은 후순위다.
5. 소프트 런치와 피처 프리즈는 품질, 서버 부하, 전환, 스토어 심사를 함께 검증하는 출시 장치다.

## 8단계 요약

### 1. 제품·기술 전제

카테고리, 서비스 모델, 플랫폼, 출시 일정, 사용자 페르소나를 정의한다. 실제 사용자(`user`)와 지불자(`payer`)를 분리하며, 유틸리티·SaaS의 팀 라이선스나 가족 요금제를 고려한다. RevenueCat/Adapty, Mixpanel/PostHog, Crashlytics 및 개인정보 보호 프레임워크를 초기 아키텍처에 포함한다.

### 2. 핵심 기능·UVP·TTV

핵심 루프를 `Trigger → Action → Outcome/Utility → Progress → Return Prompt`로 맵핑한다. UVP는 해결하는 문제와 대안보다 나은 이유를 한 문장으로 표현하고, 기능은 MoSCoW로 MVP 범위를 제한한다. TTV와 가입·권한 요청 단계의 이탈률을 계측한다.

### 3. 비즈니스 모델·페이월

구독, IAP, 광고, 하이브리드 모델을 비교하고 hard paywall(온보딩 차단)과 soft paywall(기능·사용량 제한)의 트리거를 명시한다. 스토어 수수료, 결제, API·서버 비용을 포함해 LTV, CAC, MRR/ARR, 페이월 전환율을 계산한다. 슬라이드의 `LTV > 3× CAC`는 보편 법칙이 아닌 검증할 가설이다.

### 4. 재무 모델

12~36개월 MAU·DAU, 유료 전환율, MRR/ARR, ARPU·ARPPU를 예측한다. 변동비와 고정비, 손익분기 구독자 수, 현금 소진, CAC payback, churn·expansion MRR, 사용자 증가에 따른 인프라/API 비용 확장성을 함께 산출한다.

### 5. 포지셔닝·브랜딩·ASO

진출 지역과 현지화·GDPR/CCPA를 고려하고, 직접 경쟁자뿐 아니라 수작업·종이 기록·레거시 도구 같은 간접 대안도 분석한다. 아이콘·스크린샷·영상·스토어 카피를 ASO/CRO 관점에서 A/B 테스트하고, iOS Custom Product Pages와 Google Custom Store Listings를 세그먼트별로 활용한다.

### 6. 사용자 획득

Paid(Apple Ads, Google, Meta, TikTok), Organic(ASO, 콘텐츠, web-to-app, 크리에이터), PLG(초대, 공유 워크스페이스, 워터마크, 추천 보상)를 조합한다. 테스트·스케일 예산을 나누고 CPI·CPA를 회수 기간과 연결한다. MMP와 SKAN을 고려하며, K-factor는 `사용자당 초대 수 × 초대 전환율`이다. 유틸리티 앱은 게임보다 의도 기반 검색의 비중이 크다.

### 7. 마일스톤·심사·출시

`Pre-Alpha/Feature Complete → Alpha → Feature Freeze/Beta → Release Candidate → Global Hard Launch`를 거친다. 소프트 런치에서 서버 부하, telemetry, 온보딩 실험, 전환을 검증하고 스토어 심사 버퍼 1~2주를 확보한다. 에디토리얼·PR·인플루언서 준비는 출시 6~8주 전 시작한다.

### 8. 출시 후 운영

격주 유지보수, 월간 기능, 시즌 캠페인 cadence를 정하고 키워드·스토어 자산을 지속 실험한다. 고객지원, 크래시·서버 모니터링, 퍼널 이탈, churn, 주·월 cohort의 유지율·행동·매출을 연결한다.

## 실무 체크리스트

- [ ] UVP, 핵심 사용자, 구매자 정의
- [ ] 핵심 루프·TTV·온보딩 계측 이벤트 정의
- [ ] MVP Must-have와 제외 범위 확정
- [ ] 수익 모델·페이월 트리거·스토어 비용 설계
- [ ] LTV/CAC·CAC 회수·MAU/DAU·MRR/ARR 기준선 작성
- [ ] 경쟁 대안·진출 지역·ASO 실험 계획 수립
- [ ] Paid/Organic/PLG 채널과 테스트·스케일 예산 분리
- [ ] attribution/MMP·개인정보·스토어 정책 검토
- [ ] 소프트 런치·심사 버퍼·feature freeze·출시 조건 정의
- [ ] 출시 후 업데이트·지원·모니터링·cohort 분석 책임자 지정

## AI Labs 적용 시사점

1. AI 서비스는 `사용자당 추론 비용`, 캐시율, 요청당 마진, 기능별 비용을 재무 모델에 추가해야 한다.
2. AI 핵심 루프는 `입력 → 생성 결과 → 검토/수정 → 저장·공유·재사용`으로 정의하고, TTV를 실제 업무에 쓸 수 있는 결과를 얻는 시간으로 측정한다.
3. 재생성·수정 횟수, 품질 실패, 안전 거절, 환각, 모델 장애, 비용 폭증을 일반 앱의 퍼널·서버 출시 게이트와 함께 관리한다.
4. 결과물 공유, 협업 초대, 템플릿·프롬프트 재사용은 PLG 후보지만 개인정보·저작권·비공개 설정을 함께 설계해야 한다.
5. 이 프레임워크를 AI Labs 서비스의 `제품 정의 → 단위경제 → 획득 → 운영` 공통 리뷰 템플릿으로 재사용할 수 있다.

## 사실과 해석의 구분

- 확인: 8단계, 용어, 지표, 입력 항목, 출시·운영 체크포인트는 원본 슬라이드에 명시되어 있다.
- 제안: AI API 비용, 생성 품질, 안전성, 공유·저작권을 별도 GTM 게이트로 추가하자는 내용은 AI Labs 맥락의 적용 해석이다.
- 검증 필요: 스토어 수수료·대체 결제 정책, `LTV > 3× CAC`의 적정성, 지역별 규제·심사 기준, 채널별 벤치마크.

## 후속 논의

- [ ] AI Labs 서비스 하나를 골라 8개 섹션을 실제 수치로 채운다.
- [ ] 현재 병목이 TTV, 유료 전환, CAC 회수, 모델 비용, 유지율 중 무엇인지 판단한다.
- [ ] 소프트 런치 출시 게이트와 최소 계측 이벤트를 공동 템플릿화한다.
