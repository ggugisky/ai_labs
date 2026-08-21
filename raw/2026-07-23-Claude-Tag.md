---
id: ailabs:raw/2026-07-23-claude-tag
type: Tool
status: source
created: 2026-07-23
area: ai-labs
relations:
  - type: describes
    target: ailabs:tool/claude-tag
---

# Claude Tag 분석

- Source: [GeekNews topic 30809](https://news.hada.io/topic?id=30809)
- Anthropic blog: [Introducing Claude Tag](https://www.anthropic.com/news/introducing-claude-tag)
- Docs: [Work with Claude Tag](https://claude.com/docs/claude-tag/overview)

## 한줄 요약

Claude Tag는 Slack 안에서 `@Claude`로 작업을 위임하고, 채널 단위 권한과 메모리, 비동기 실행, 감사 가능한 결과물을 제공하는 팀용 에이전트 기능이다.

## 핵심 포인트

- Slack 채널, 스레드, DM에서 동작한다.
- 팀이나 조직 단위로 연결된 도구, 데이터, 코드베이스를 사용한다.
- 작업은 스레드 안에서 체크리스트 형태로 진행 상황이 보인다.
- 결과는 같은 스레드에 남아서 다른 팀원이 이어받을 수 있다.
- 채널별 접근 권한, 조직별 지출 한도, 작업 로그를 관리자가 제어한다.

## 왜 중요한가

- 개인용 챗봇이 아니라 팀 협업용 에이전트로 설계됐다.
- 핵심은 모델 자체보다 `identity`, `access scope`, `memory`, `audit trail`이다.
- Slack이라는 기존 업무 동선에 바로 붙기 때문에 사용 장벽이 낮다.
- 비동기 작업과 후속 추적이 자연스럽게 설계되어 있다.

## 눈여겨볼 점

- 채널 단위로 메모리와 권한을 나누는 구조가 강하다.
- 작업이 끝나면 스레드에 결과가 남아 협업 기록이 된다.
- 관리자는 채널별 도구 접근과 예산을 통제할 수 있다.
- 조직 내부에서는 코드 작성뿐 아니라 지표 확인, 지원 티켓, 버그 원인 분석까지 확장할 수 있다.

## 한계와 주의점

- Team/Enterprise와 Slack 중심이라 사용 범위가 제한적이다.
- 채널 메모리가 강해질수록 프라이버시와 권한 분리가 더 중요해진다.
- 조직 전체를 대상으로 하는 만큼 비용 통제가 필요하다.
- 공유형 에이전트는 개인형 에이전트보다 설계 복잡도가 높다.

## AI Labs 토론 질문

- 우리 쪽에 필요한 건 개인형 에이전트인가, 채널형 에이전트인가?
- 팀용 에이전트를 만들 때 가장 먼저 풀어야 할 문제는 모델 성능인가, 권한 모델인가?
- 채널 단위 메모리와 개인 단위 메모리를 어떻게 분리할 것인가?
- 결과물을 스레드에 남기는 방식이 실제 협업에 어떤 차이를 만드는가?
- 이 구조를 내부 업무 도구에 적용한다면 Slack 외 어떤 인터페이스가 더 적절한가?

## 메모

- 이 기능은 "Slack에 붙은 챗봇"보다 "조직용 지속 에이전트"에 가깝다.
- 에이전트 플랫폼을 설계할 때 제품화 포인트는 모델보다 운영 경계와 감사 가능성에 있다.
