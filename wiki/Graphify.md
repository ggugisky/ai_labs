---
id: ailabs:wiki/graphify
type: Tool
tags: [ai, knowledge-graph, llm-wiki, coding-agent, local]
created: 2026-08-22
status: reviewed
area: ai-labs
relations:
  - type: discussed_in
    target: ailabs:raw/meeting/20260724
  - type: related_to
    target: ailabs:wiki/llm-wiki
  - type: describes
    target: ailabs:tool/graphify
provenance:
  sources:
    - id: ailabs:raw/meeting/20260724
      role: meeting
      captured_at: 2026-07-24
    - url: https://graphify.com/docs
      role: official
      accessed_at: 2026-08-22
---

# Graphify

> Current source: [Graphify](https://graphify.com/), [Quickstart](https://graphify.com/docs), [Graphify GitHub](https://github.com/Graphify-Labs/graphify)
> Meeting link: `https://github.com/graphifylabs/graphify` (현재는 404이며, 공식 경로가 `Graphify-Labs/graphify`로 변경된 것으로 보임)
> Meeting: [[raw/meeting/20260724]]

## 한줄 요약

Graphify는 코드·문서·데이터의 구조를 온디바이스 지식 그래프로 만들고, AI coding assistant가 파일을 매번 다시 읽는 대신 그래프를 탐색하도록 하는 LLM Wiki 확장 도구다.

## 핵심 동작

1. `graphify` CLI와 assistant용 skill을 설치한다.
2. 프로젝트에서 `/graphify .`를 실행한다.
3. 코드 파일은 tree-sitter 기반으로 로컬 파싱한다.
4. 함수, 클래스, 파일, 테이블, 문서와 그 관계를 그래프 노드·엣지로 만든다.
5. `graph.html`, `GRAPH_REPORT.md`, `graph.json`을 생성한다.
6. AI assistant가 그래프를 질의해 구조와 근거 경로를 확인한다.

## LLM Wiki와의 차이

LLM Wiki가 원문을 구조화된 Markdown 문서로 정리해 에이전트가 읽기 좋게 만드는 방식이라면, Graphify는 명시적인 관계와 경로를 가진 지식 그래프를 추가한다.

- LLM Wiki: 사람이 읽고 수정하기 좋은 문서 중심
- Graphify: 관계 탐색과 구조 질의에 강한 그래프 중심
- 결합 방식: Markdown 문서를 원천으로 두고 Graphify를 탐색·검증·요약 계층으로 사용

## 정확성과 비용 관리

- 코드 구조 추출은 로컬·결정론적 파싱을 사용해 모델 호출을 줄인다.
- 문서·PDF·이미지·SQL·Terraform 등은 설정한 모델을 이용한 semantic pass가 필요할 수 있다.
- 관계마다 `EXTRACTED`, `INFERRED`, `AMBIGUOUS`처럼 근거 수준을 구분할 수 있다.
- 답변에 파일·라인 경로를 남기면 결과를 검증하기 쉽다.

## 장점

- 코드베이스의 구조를 매번 재발견하는 토큰 비용을 줄일 수 있다.
- 그래프 시각화로 모듈·커뮤니티·핵심 노드를 파악하기 쉽다.
- 관계와 출처를 명시해 단순 벡터 검색보다 구조 질의에 강하다.
- Codex, Claude Code, Cursor 등 여러 assistant에 연결할 수 있다.
- 로컬 우선 구조라 민감한 코드의 외부 전송을 줄일 수 있다.

## 한계와 주의점

- 그래프가 최신 상태가 아니면 assistant의 판단도 오래된 구조에 의존한다.
- 문서나 비정형 자료의 semantic extraction은 모델 품질과 비용에 영향을 받는다.
- 추출된 관계와 추론된 관계를 섞으면 지식 그래프가 과신을 만들 수 있다.
- Graphify는 지식의 원천 저장소가 아니라 탐색·구조화 계층으로 두는 편이 안전하다.

## AI Labs 시사점

Graphify는 현재 AI Labs의 `raw/wiki` 구조와 직접 연결된다. 원문을 Markdown/Git에 보존하고, Graphify를 구조 탐색 계층으로 추가하면 LLM Wiki의 재탐색 비용과 관계 검색 한계를 보완할 수 있다. 다만 raw와 graph의 source of truth를 명확히 분리해야 한다.
