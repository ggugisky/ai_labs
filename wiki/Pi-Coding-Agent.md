---
tags: [ai, agent, harness, coding, extensibility]
created: 2026-08-21
status: reviewed
area: ai-labs
---

# Pi Coding Agent

> Source: [Pi official site](https://pi.dev/), [Pi usage documentation](https://pi.dev/docs/latest/usage), [Pi security documentation](https://pi.dev/docs/latest/security)
> Meeting: [[raw/meeting/20260821]]

## 한줄 요약

Pi는 기능이 많은 완제품형 코딩 에이전트보다, 확장·스킬·프롬프트·패키지를 조합해 사용자가 직접 workflow를 만드는 최소형 agent harness다.

## 핵심 특징

- Interactive TUI, print/JSON, RPC, SDK 네 가지 실행 모드
- 여러 모델·provider를 연결하고 세션 중 모델을 전환
- TypeScript extensions, skills, prompt templates, themes 지원
- npm 또는 Git 기반 Pi package 공유
- 트리 구조 세션 기록과 이전 분기점으로의 복귀
- `AGENTS.md`, `SYSTEM.md`, project skills를 통한 context engineering
- 자동 compaction과 확장 가능한 memory·RAG 구성

## 의도적으로 제공하지 않는 것

Pi는 핵심을 작게 유지하기 위해 다음 기능을 기본 제공하지 않는다.

- MCP
- sub-agents
- plan mode
- permission popup
- 내장 sandbox
- background bash

이 기능들은 확장 프로그램, 패키지, 외부 도구로 직접 구성해야 한다. 따라서 Pi는 즉시 완성된 업무 프로세스를 제공하는 제품이라기보다, 에이전트 런타임의 기본 부품을 제공하는 쪽에 가깝다.

## 장점

- 사용자의 workflow를 제품의 기본 흐름에 맞출 필요가 적다.
- 확장 기능을 직접 만들고 `/reload`로 즉시 반영할 수 있다.
- 모델 provider와 실행 모드를 분리해 실험하기 좋다.
- 세션 tree와 Markdown 기반 context 파일이 하네스 실험에 잘 맞는다.
- SDK·RPC를 이용해 다른 시스템에 내장할 수 있다.

## 한계와 보안 주의점

- sub-agent, 권한 승인, sandbox가 기본이 아니어서 직접 설계해야 한다.
- 로컬 coding agent로 실행되며 시작한 사용자 계정의 권한을 사용한다.
- project trust는 sandbox가 아니고, 신뢰한 프로젝트의 확장·스킬이 실행할 수 있는 범위를 제한하지 않는다.
- 외부 저장소의 prompt injection이나 악성 확장 기능에 대한 방어를 별도로 마련해야 한다.

## AI Labs 시사점

Pi는 AI Labs의 “하네스를 직접 만든다”는 방향과 잘 맞는다. 특히 기본 기능을 덜어내고 `skills`, `AGENTS.md`, extensions, packages를 조합하는 방식은 LLM Wiki와 개인 workspace를 에이전트 실행 규칙으로 연결하는 모델로 참고할 수 있다.

반대로 권한 승인·sandbox·sub-agent를 기본 제공하지 않는 선택은 Margaret 같은 Gateway에서 별도의 policy layer가 필요하다는 점을 보여준다.

## Connect AI와의 비교

- Connect AI: IDE와 로컬 모델, 지식 구조화에 가까운 통합형 확장
- Pi: 최소 코어와 확장 API를 제공하는 조립형 coding agent

둘 다 하네스 중심이지만, Connect AI가 완성된 지식·IDE 경험을 제공하려는 쪽이라면 Pi는 사용자가 원하는 실행 모델을 직접 설계하도록 더 많이 위임한다.

