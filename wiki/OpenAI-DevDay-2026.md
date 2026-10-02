---
id: ailabs:wiki/openai-devday-2026
type: Document
title: OpenAI DevDay 2026
tags: [openai, devday, agents, multi-agent, codex, computer-use, llm-wiki]
created: 2026-10-02
status: reviewed
area: ai-labs
relations:
  - type: derived_from
    target: ailabs:raw/2026-10-02-openai-devday-2026
  - type: related_to
    target: ailabs:wiki/connect-ai
  - type: related_to
    target: ailabs:wiki/graphify
  - type: related_to
    target: ailabs:wiki/llm-wiki
  - type: related_to
    target: ailabs:use-case/creative-content-production
provenance:
  sources:
    - id: ailabs:raw/2026-10-02-openai-devday-2026
      role: captured_video_summary
      captured_at: 2026-10-02
    - url: https://www.youtube.com/watch?v=GjN3xLDuc8o
      role: shared_video
      accessed_at: 2026-10-02
    - url: https://developers.openai.com/api/docs/models/gpt-6.1-sol
      role: official
      accessed_at: 2026-10-02
    - url: https://developers.openai.com/api/docs/changelog
      role: official
      accessed_at: 2026-10-02
    - url: https://developers.openai.com/api/docs/guides/tools-computer-use
      role: official
      accessed_at: 2026-10-02
    - url: https://developers.openai.com/cookbook/topic/agents
      role: official
      accessed_at: 2026-10-02
---

# OpenAI DevDay 2026

> Shared video: [OpenAI Dev Day 2026: Everything Announced in 15 Minutes](https://www.youtube.com/watch?v=GjN3xLDuc8o)

## 한줄 요약

OpenAI DevDay 2026의 중심은 새 모델 하나보다, 지속형 에이전트·멀티 에이전트 위임·컴퓨터 사용·클라우드 실행·팀 협업·보안 검증을 하나의 업무 플랫폼으로 묶는 방향이다.

## 기능별 요약

### 1. Dots

사용자가 자리를 비운 동안에도 작업을 계속하는 지속형 에이전트다. 연결된 앱과 클라우드 컴퓨터를 사용하고, 업무 채널에 참여하는 방향으로 소개되었다. 기업용 Specialist Dots는 조직 내 특정 책임을 맡는 전문 에이전트 모델이다.

### 2. 멀티 에이전트 위임

하나의 에이전트가 조사·작성·코딩·검증 같은 하위 작업을 나누어 다른 에이전트에 위임하는 구조다. API changelog에도 GPT-6.1 Sol의 멀티 에이전트 위임이 베타 기능으로 기록되어 있다.

### 3. ChatGPT Space와 Pages

사람과 에이전트가 파일·페이지·프로젝트 맥락을 공유하는 협업 공간이다. 문서를 편집하고 차트나 인터랙티브 결과물을 함께 만들 수 있으며, 팀 작업과 반복 작업 할당으로 확장된다.

### 4. Slack·Teams 연동

업무 채널에서 에이전트를 호출하고 연결된 도구를 사용할 수 있는 흐름이다. 에이전트의 답변보다 채널 맥락, 권한, 승인, 실행 로그가 핵심 운영 요소가 된다.

### 5. GPT-6.1 Sol

복잡한 코딩·컴퓨터 사용·전문 업무에서 Astra에 가까운 성능을 더 낮은 비용으로 제공하는 모델로 문서화되어 있다. Responses API 도구 호출, 구조화 출력, 컴퓨터 사용, MCP를 지원한다.

공식 모델 문서의 표준 가격은 입력 1M 토큰 2달러, 캐시 입력 0.10달러, 출력 1M 토큰 10달러다. 실제 작업 비용은 도구 호출, 재시도, 컨텍스트 길이에 따라 달라지므로 자체 데이터로 비교해야 한다.

### 6. Astra Ultrafast

품질 모델을 바꾸기보다 출력 토큰 사이의 지연을 줄이는 처리 모드다. 실시간 코딩·데모에는 유용하지만 반복 자동화에서는 속도 향상이 추가 비용을 정당화하는지 확인해야 한다.

### 7. Decisions API와 Luna

자유로운 장문 생성보다 분류·라우팅·정해진 선택지 중 결정하는 업무에 맞는 방향이다. 문서 분류, 담당 에이전트 배정, 사람 검토 여부 판정에 적용할 수 있다.

### 8. Agents API 컴퓨터 사용

에이전트가 브라우저나 데스크톱 UI를 보고 조작한다. OpenAI 문서는 애플리케이션이 실행 루프, 승인, 로그인, 권한을 관리하는 구조를 전제로 한다. 화면의 텍스트가 사용자의 지시를 덮어쓸 수 없도록 설계해야 한다.

### 9. Codex Cloud·CLI·Code Review

Codex 작업을 클라우드에서 장시간 실행하고, CLI에서 여러 에이전트와 세션을 관리하며, 변경 사항을 요약·검토하는 흐름이다. 로컬 코딩 보조에서 원격 작업 오케스트레이션으로 확장된 사례다.

### 10. Codex Security Cloud

코드베이스 위협 모델을 바탕으로 취약점 후보를 조사하고, 공격 경로를 검증하고, 패치를 제안하는 보안 작업 흐름이다. 결과를 자동 반영하기보다 사람이 검토할 수 있는 증거와 수정안을 제공하는 점이 중요하다.

### 11. Plugins, MCP events, Marketplace

플러그인 UI 확장, MCP 기반 자동화 트리거, ChatGPT 계정 인증, 기업용 파트너 소프트웨어 유통을 통해 OpenAI를 모델 제공자를 넘어 에이전트·앱 플랫폼으로 확장하려는 방향이다.

## 사실과 해석의 구분

### 확인된 사실

- 영상은 위 기능들을 DevDay 2026의 주요 발표로 소개한다.
- GPT-6.1 Sol, 컴퓨터 사용, 멀티 에이전트 위임, Ultrafast는 공식 개발자 문서와 changelog에서 확인된다.
- OpenAI 개발자 문서는 에이전트를 도구를 사용해 독립적으로 작업하는 시스템으로 설명하고, 명확한 가드레일을 요구한다.

### 해석

- 경쟁의 중심이 모델 단품에서 에이전트의 실행 환경·권한·메모리·협업·검증 계층으로 이동하고 있다.
- Dots와 Space는 개인 생산성 도구라기보다 사람과 에이전트가 함께 일하는 작업 운영체제에 가깝다.
- 에이전트가 많아질수록 생성 능력보다 비용, 승인, 중복 실행, 실패 복구, 감사 로그가 병목이 될 가능성이 높다.

### 한계와 미확인 사항

- 영상 데모만으로 장시간 작업의 안정성, 실제 실패율, 총비용을 판단할 수 없다.
- 제품별 출시 범위와 계정·지역별 이용 가능 여부는 변할 수 있다.
- 모델의 “Astra에 가까운 성능”은 자체 평가와 특정 조건에 따른 표현이며 AI Labs 업무에서 재현된 결과가 아니다.
- 컴퓨터 사용과 Slack·Teams 연동은 권한 오남용, 프롬프트 인젝션, 민감정보 노출 위험을 가진다.

## AI Labs 연결 포인트

### Connect AI와 하네스

`connect-ai`의 CEO·비서·개발자·리서처 등 역할 분리 구조를 Specialist Dots와 비교할 수 있다. 비교 기준은 역할 정의, 메모리 분리, 도구 권한, 핸드오프 성공률, 실패 복구다.

### LLM Wiki와 Graphify

Space가 협업 표면이라면 LLM Wiki는 Git 기반 원천 지식 저장소가 될 수 있다. Graphify는 문서와 관계를 탐색하는 계층으로 사용하고, 에이전트 답변에는 원문 경로와 `EXTRACTED`·`INFERRED` 수준을 남기는 것이 안전하다.

### 콘텐츠 제작 파이프라인

주제 조사 → 대본 → 이미지·영상·TTS → 품질검수 → 게시 → 성과분석 흐름에 전문 에이전트를 배치할 수 있다. 게시·외부 메시지·결제·저작권 판단은 사람 승인 게이트를 둔다.

## 후속 실험 제안

1. **Wiki 승격 게이트**: Decisions API 또는 구조화 출력을 이용해 raw 문서를 `wiki 후보`, `추가 검증`, `보류`로 분류한다. 정확도·근거성·사람 검토 시간을 측정한다.
2. **멀티 에이전트 비교**: Connect AI 방식과 단일 에이전트 방식을 같은 회의록 20건에 적용해 누락 액션아이템, 잘못된 추론, 비용, 처리 시간을 비교한다.
3. **컴퓨터 사용 안전 실험**: 비생산용 계정과 샌드박스 사이트에서만 브라우저 작업을 실행하고, 승인·중단·실패복구·로그 완전성을 평가한다.
4. **Codex식 검증 루프**: Graphify/Obsidian 플러그인에 대해 위협 모델 → 취약점 후보 → 재현 테스트 → 패치 제안 → 사람 승인 흐름을 설계한다.

## LLM Wiki 등재 후보

- `지속형 에이전트의 권한·승인·감사 설계`
- `멀티 에이전트 하네스 평가 기준`
- `컴퓨터 사용 에이전트의 안전한 실행 루프`
- `생성보다 검증을 우선하는 Codex Security식 워크플로`
- `LLM Wiki의 raw → 검토 → wiki 승격 게이트`
