---
id: ailabs:wiki/claude-tag
type: Tool
tags: [ai, agent, collaboration, slack, memory, governance]
created: 2026-08-21
status: reviewed
area: ai-labs
relations:
  - type: discussed_in
    target: ailabs:raw/meeting/20260821
  - type: derived_from
    target: ailabs:raw/2026-07-23-claude-tag
  - type: describes
    target: ailabs:tool/claude-tag
provenance:
  sources:
    - id: ailabs:raw/2026-07-23-claude-tag
      role: analysis
      captured_at: 2026-07-23
    - url: https://www.anthropic.com/news/introducing-claude-tag
      role: official
      accessed_at: 2026-08-22
---

# Claude Tag

> Source: [Anthropic announcement](https://www.anthropic.com/news/introducing-claude-tag), [Claude Help Center](https://support.claude.com/en/articles/15594475-what-is-claude-tag)
> Raw note: [[raw/2026-07-23-Claude-Tag]]
> Meeting: [[raw/meeting/20260821]]

## 한줄 요약

Claude Tag는 Slack 채널에 `@Claude`를 호출해 팀의 도구·데이터·코드베이스를 사용하게 하는 조직용 협업 에이전트다.

## 핵심 동작

- Slack 채널과 스레드에서 `@Claude`로 작업을 위임한다.
- Claude가 조직의 별도 identity로 동작한다.
- 채널에 연결된 도구, 저장소, 데이터에 접근해 비동기 작업을 수행한다.
- 진행 상황과 결과가 같은 스레드에 남아 팀원이 확인하고 이어받을 수 있다.
- 작업 완료 후 후속 알림이나 재확인을 스스로 수행할 수 있다.
- 채널 단위의 context와 memory를 사용한다.

## 개인용 Claude와 다른 점

Claude Tag는 개인 채팅창에 질문하는 기능이 아니라 팀 작업 공간에 들어온 공유 에이전트에 가깝다.

- 채널에 참여한 구성원이 같은 Claude의 작업 맥락을 본다.
- 채널 작업은 조직이 설정한 도구와 권한을 사용한다.
- 채널 작업 비용은 조직 사용량으로 관리된다.
- DM이나 개인 assistant panel은 개인 계정의 권한·대화 기록과 분리된다.

## 운영·거버넌스 포인트

- 관리자만 Claude identity, 연결 도구, 저장소, 허용 채널을 설정한다.
- 멤버 접근 권한을 조직 전체, Claude 조직 멤버, 특정 역할 등으로 제한할 수 있다.
- 사용량 기반 지출 한도를 설정할 수 있다.
- 채널 경계를 넘지 않도록 memory와 activity를 관리해야 한다.
- Slack 대화 기록과 Claude 웹앱 대화 기록은 서로 분리된다.

## 장점

- 팀이 이미 사용하는 Slack 안에서 시작할 수 있다.
- 작업 과정이 스레드에 남아 협업과 감사가 쉽다.
- 개인별 챗봇이 아니라 공유 context를 가진 팀 에이전트로 사용할 수 있다.
- 코드, 지표, 지원 티켓, 버그 분석 등 비개발 업무에도 적용 가능하다.

## 한계와 주의점

- Slack과 Team·Enterprise 플랜을 전제로 한다.
- 채널 memory가 강해질수록 잘못된 정보와 민감정보의 확산 위험이 커진다.
- 공유 에이전트는 개인 에이전트보다 권한·비용·책임 경계가 복잡하다.
- 채널에서 보이는 작업과 실제 외부 시스템 변경 사이에 승인 단계를 둬야 한다.

## AI Labs 시사점

Claude Tag의 핵심은 모델 성능보다 `identity + access scope + shared memory + audit trail`이다. Margaret Gateway나 AI Community용 Agent를 설계할 때도 채널별 agent identity, 권한 범위, 결과 기록, 비용 통제를 1급 개념으로 두는 참고 사례가 된다.

## 토론 질문

- 개인 메모리와 채널 메모리를 어떤 규칙으로 분리할 것인가?
- Slack 스레드에 남은 결과를 공식 지식으로 승격하는 기준은 무엇인가?
- 조직용 에이전트의 외부 실행은 어떤 작업부터 승인 대상으로 둘 것인가?
