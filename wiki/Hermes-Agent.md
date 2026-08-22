---
id: ailabs:wiki/hermes-agent
type: Agent
tags: [ai, agent, memory, skills, automation, multi-channel]
created: 2026-08-22
status: reviewed
area: ai-labs
relations:
  - type: discussed_in
    target: ailabs:raw/meeting/20260626
---

# Hermes Agent

> Source: [Hermes Agent official documentation](https://hermes-agent.nousresearch.com/docs/), [GitHub](https://github.com/NousResearch/hermes-agent)
> Meeting: [[raw/meeting/20260626]]

## 한줄 요약

Hermes Agent는 경험에서 스킬과 기억을 만들고 개선하는 학습 루프를 내장한 멀티채널 자율 에이전트다.

## 핵심 기능

- 세션 간 지속 memory와 사용자 모델링
- 경험에서 procedural skill을 만들고 재사용·개선
- CLI, desktop, Telegram, Discord, Slack, WhatsApp 등 멀티채널 gateway
- 로컬·Docker·SSH·Daytona·Modal 등 여러 실행 backend
- web search, browser, image generation, vision, TTS 등 도구 연결
- MCP integration과 isolated subagent delegation
- cron 기반 예약 작업 및 채널별 결과 전달
- Bot Mode에서 이름·모델·메모리·스킬·루틴이 분리된 전문 Bot 구성

## LLM Wiki와의 관계

Hermes의 memory와 skills는 LLM Wiki와 비슷하게 지식을 다음 작업에 재사용한다. 그러나 초점은 정적인 문서 저장보다 에이전트가 경험을 통해 절차와 사용자 맥락을 계속 축적하는 데 있다.

- LLM Wiki: 사람이 검토하고 Git으로 관리하는 명시적 지식
- Hermes memory: 세션 간 사용자·프로젝트 맥락을 회상하는 지속 기억
- Hermes skills: 반복 업무를 수행하는 절차적 기억

따라서 Hermes를 사용할 때도 자동 생성 memory를 바로 공식 wiki로 승격하기보다, 검토·정제·승격 단계를 별도로 두는 것이 좋다.

## 실행 구조

1. CLI·desktop·메시징 채널 중 하나로 요청을 받는다.
2. agent가 memory, skills, context files를 조합한다.
3. terminal, browser, web, MCP, delegation 도구를 사용한다.
4. 필요한 경우 subagent를 병렬 실행한다.
5. 결과를 현재 채널에 전달하고, 향후 재사용할 memory·skill을 갱신한다.

Nous Portal을 사용하면 하나의 OAuth와 subscription으로 모델 및 web·image·TTS·browser Tool Gateway를 묶을 수 있다. 반대로 OpenRouter, OpenAI 또는 다른 endpoint를 직접 연결하는 구성도 가능하다.

## 장점

- 개인 비서·장기 학습·반복 업무 자동화에 적합하다.
- 채널·실행 환경·도구를 분리해 어디서든 같은 agent를 이어 쓸 수 있다.
- memory와 skills가 제품의 중심이라 장기적인 개인화가 쉽다.
- subagent, MCP, cron을 조합해 복합 workflow를 만들 수 있다.

## 한계와 주의점

- 자동 학습 memory가 잘못된 사실이나 실패한 절차를 축적할 수 있다.
- 터미널·브라우저·메시징 권한을 함께 주면 영향 범위가 커진다.
- 멀티채널에서 동일한 memory를 공유할 때 개인정보와 조직 정보의 경계를 관리해야 한다.
- Tool Gateway와 모델 provider를 사용하면 비용과 데이터 처리 경로를 확인해야 한다.
- 장기 실행 에이전트는 승인, 격리, 로그, 실패 복구를 기본 설계에 포함해야 한다.

## AI Labs 시사점

첫 미팅에서 Hermes Agent를 LLM Wiki와 함께 이야기한 이유는 `기억하는 에이전트`와 `검토 가능한 지식 저장소`의 결합 가능성 때문이다. AI Labs의 raw/wiki 구조를 Hermes의 memory·skills와 연결할 때는 자동 기록과 공식 지식 승격을 분리하는 운영 규칙이 핵심이다.

