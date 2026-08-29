---
id: ailabs:wiki/crack
type: Service
tags: [ai, consumer-ai, character-ai, storytelling, roleplay, ugc, content, monetization]
created: 2026-08-29
status: reviewed
area: ai-labs
relations:
  - type: describes
    target: ailabs:service/crack
  - type: derived_from
    target: ailabs:raw/2026-08-29-crack
  - type: related_to
    target: ailabs:service/modu-ui-gaesori
  - type: related_to
    target: ailabs:service/dalar
  - type: related_to
    target: ailabs:service/lampas
  - type: related_to
    target: ailabs:tool/connect-ai
  - type: related_to
    target: ailabs:service/ssot-viewer
  - type: supports
    target: ailabs:use-case/creative-content-production
provenance:
  sources:
    - id: ailabs:raw/2026-08-29-crack
      role: analysis
      captured_at: 2026-08-29
    - url: https://help.crack.wrtn.ai/
      role: official-help
      accessed_at: 2026-08-29
    - url: https://help.crack.wrtn.ai/guide/creator/info/what-is-crack-originals
      role: official-creator-policy
      accessed_at: 2026-08-29
    - url: https://openai.com/ko-KR/index/wrtn/
      role: product-case-study
      accessed_at: 2026-08-29
    - url: https://www.mk.co.kr/news/business/12016636
      role: interview-and-financial-context
      accessed_at: 2026-08-29
---

# 크랙(Crack)

> 한국 뤼튼의 AI 캐릭터·대화형 스토리 플랫폼. 일본의 캬라푸, 북미의 OOC로 현지화된다.

## 한줄 요약

크랙은 범용 AI 챗봇이 아니라 `웹소설·게임·캐릭터 챗`을 AI 대화로 결합한 소비자 콘텐츠 플랫폼이다. 사용자는 캐릭터와 이야기를 소비하면서 동시에 직접 캐릭터와 스토리를 제작한다.

## 서비스 경험

- 캐릭터의 성격, 말투, 배경, 관계를 설정한 대화
- 1 대 1 롤플레잉과 여러 인물이 등장하는 시뮬레이션
- 이용자가 주인공처럼 행동하며 AI가 다음 장면과 대사를 생성하는 인터랙티브 스토리
- 이미지, 상태창, 시리즈·세계관을 결합한 콘텐츠
- 이용자가 만든 캐릭터·스토리를 다른 이용자가 발견하고 소비하는 UGC

공식 가이드는 기본, 1 대 1 롤플레잉, 시뮬레이션, 생산성, 제작자 커스텀 프롬프트를 구분한다. 이용자는 튜토리얼을 통해 캐릭터와 스토리를 직접 만들 수 있다. [크랙 고객센터](https://help.crack.wrtn.ai/)

## 수익모델

크랙은 `크래커`라는 서비스 내 재화를 사용한다. 크래커는 구매하거나 출석·도전과제로 얻을 수 있고, 선택한 대화 모드에 따라 소모된다. 따라서 무료 유입 후 몰입도가 높은 대화·콘텐츠에서 반복 결제를 유도하는 모바일 콘텐츠 플랫폼형 모델이다. [크래커 안내](https://help.crack.wrtn.ai/)

크랙 오리지널은 플랫폼이 작품의 저작권을 구매하고, 해당 콘텐츠에서 발생한 유료 크래커의 5%를 창작자에게 현금 정산한다. 선정작은 OOC와 캬라푸에 번역·공개될 수 있으며, 글로벌 유료 재화 사용량도 별도 정산 대상이다. [크랙 오리지널 정책](https://help.crack.wrtn.ai/guide/creator/info/what-is-crack-originals)

## 사업적 의미

크랙의 방어력은 모델 자체보다 한국어 말투·문화에 맞춘 캐릭터 UX, 축적되는 콘텐츠 라이브러리, 크리에이터 네트워크, 반복 대화·결제, 글로벌 현지화 경로의 조합에서 나온다.

뤼튼은 크랙을 통해 생산성 중심 AI에서 라이프스타일·엔터테인먼트 AI로 확장했다고 설명한다. 다만 2025년 뤼튼 전체 매출은 471억 원, 영업손실은 약 588억 원으로 공개돼 있어 크랙을 확정적인 고수익 캐시카우라고 부르기에는 이르다. 사업별 매출·이익은 별도 검증이 필요하다. [OpenAI 사례](https://openai.com/ko-KR/index/wrtn/), [매일경제](https://www.mk.co.kr/news/business/12016636)

## AI Labs 기존 서비스에 미치는 전략적 영향

### 모두의 개소리: 요약 채널에서 참여형 미디어로

현재 `모두의 개소리`의 영상 수집 → 요약 → 대본·에셋 생성 → 업로드·성과분석 파이프라인을, 가상의 진행자·정치 풍자 캐릭터·쟁점별 토론 캐릭터가 있는 대화형 뉴스 경험으로 확장할 수 있다. 쇼츠는 유입, 캐릭터 대화는 체류·재방문 채널로 설계한다. 실존 인물·정치 이슈는 명예훼손, 편향, 허위정보, 저작권 검수가 선행되어야 한다.

### Dalar·Lampas: 생성 도구를 세계관 제작 스튜디오로

`Dalar`의 레퍼런스 일관성 유지와 `Lampas`의 노드형 이미지·영상 파이프라인을 캐릭터 시트, 장소 레퍼런스, 에피소드 썸네일, 장면 에셋 제작에 결합한다. 목표는 `세계관 설계 → 대화 → 장면 생성 → 시리즈화`다.

### connect-ai: 에이전트 팀을 콘텐츠 제작사로

`connect-ai`의 분업 구조를 작가·리서처·팩트체커·대화 설계자·이미지/영상 제작자·안전검수·배포/분석 에이전트로 확장한다. 에이전트 수보다 검수·승인·회고 기록을 저장소에 남기는 운영이 핵심이다.

### SSOT Viewer: 캐릭터·콘텐츠 지식 그래프

`캐릭터 → 세계관 → 에피소드 → 프롬프트 → 생성 에셋 → 출처 → 검수 결과 → 성과`를 연결하면 콘텐츠 운영용 SSOT가 된다. 어떤 설정이 재방문을 만들었는지, 어떤 프롬프트가 품질 저하를 일으켰는지, 에셋의 권리 상태가 무엇인지 추적할 수 있다.

## AI Labs 다음 실험

1. `모두의 개소리` 이슈 하나로 진행자·찬반·팩트체커 캐릭터 3종의 프로토타입 제작
2. Dalar·Lampas로 캐릭터 시트와 3개 장면 에셋 생성
3. connect-ai로 리서치·대본·안전검수 연결
4. SSOT Viewer에 캐릭터·출처·프롬프트·검수 상태 등록
5. 10명 내외 테스트에서 재방문 의향, 대화 지속률, 사실성 평가, 유료 가치 인식 측정

## 확인 지표

- 캐릭터별 1일·7일 잔존율
- 대화 세션 길이와 재방문율
- 유료 전환율·이용자당 매출
- 대화 1회당 모델 비용과 콘텐츠 마진
- 설정 이탈률과 안전 필터 오탐·미탐률
- 창작자 콘텐츠의 생산량·조회·결제·재사용률
