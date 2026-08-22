---
id: ailabs:wiki/grok-bot
type: Service
tags: [ai, agent, computer-use, automation, xai]
created: 2026-08-21
status: reviewed
area: ai-labs
relations:
  - type: discussed_in
    target: ailabs:raw/meeting/20260821
  - type: describes
    target: ailabs:service/grok-bot
provenance:
  sources:
    - id: ailabs:raw/meeting/20260821
      role: meeting
      captured_at: 2026-08-21
    - url: https://x.ai/bot
      role: official
      accessed_at: 2026-08-22
---

# Grok Bot

> Source: [Grok Bot official site](https://x.ai/bot)
> Meeting: [[raw/meeting/20260821]]

## 한줄 요약

Grok Bot은 사용자의 컴퓨터와 웹 앱에 로그인해 사람처럼 작업하고, 여러 Bot이 병렬로 협업하며, 반복 작업을 routine으로 저장해 계속 실행하는 컴퓨터 사용형 AI 동료다.

## 핵심 기능

- 데스크톱·모바일에서 Bot에게 자연어로 업무를 위임
- Bot마다 영업, 리서치, 고객지원, 버그 재현 등 역할 지정
- 여러 Bot을 동시에 실행하고 Bot끼리 작업을 전달
- 사용자가 한 번 보여준 작업을 routine으로 저장해 재실행
- 로그인된 웹사이트와 앱을 직접 사용
- 작업 중 사용자의 승인이 필요한 시점에 돌아와 확인 요청
- 자체 computer와 일정 실행을 포함한 상시 업무 흐름

## 기존 API 에이전트와 다른 점

Grok Bot은 모든 서비스를 API로 연결하는 대신, 사용자가 브라우저와 앱에서 하는 동작을 직접 수행하는 방향이다. 따라서 API가 없거나 UI가 복잡한 업무도 자동화할 수 있지만, 동시에 화면·로그인·권한 변화에 민감한 자동화가 된다.

## 장점

- 기존 웹 업무를 API 개발 없이 자동화할 가능성이 있다.
- 여러 Bot을 역할별로 나눠 팀처럼 운용할 수 있다.
- 반복 업무를 routine으로 만들어 비동기·주기적으로 실행할 수 있다.
- 영업, 고객지원, 리서치, 운영 등 코딩 외 업무에 적용하기 쉽다.

## 한계와 주의점

- 로그인된 계정과 브라우저 권한을 사용하므로 계정 탈취·오작동의 영향이 크다.
- UI가 바뀌면 routine이 깨질 수 있다.
- 메시지 발송, 결제, 게시, 데이터 변경은 명시적 승인과 실행 로그가 필요하다.
- 여러 Bot이 병렬로 움직일 때 중복 실행과 충돌을 제어해야 한다.
- 공식 사이트의 benchmark 수치는 자체 소개 자료이므로 실제 업무 환경에서 별도 검증해야 한다.

## AI Labs 시사점

Grok Bot은 `agent = model + tools`를 넘어 `agent = model + computer + account + routine`으로 확장되는 사례다. Margaret의 adapter나 Gateway에서 브라우저·외부 계정을 연결할 때, 계정별 scope와 승인 상태를 세션의 1급 정보로 관리해야 한다는 점을 보여준다.
