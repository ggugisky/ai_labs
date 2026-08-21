---
id: ailabs:raw/2026-07-23-open-knowledge-format
type: Concept
status: source
created: 2026-07-23
area: ai-labs
relations:
  - type: supports
    target: ailabs:wiki/llm-wiki
---

# Open Knowledge Format 분석

- Source: [GeekNews topic 30622](https://news.hada.io/topic?id=30622)
- Google Cloud Blog: [How the Open Knowledge Format can improve data sharing](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)

## 한줄 요약

Google의 Open Knowledge Format(OKF)은 내부 지식을 `Markdown + YAML frontmatter` 기반의 디렉터리 번들로 표준화해서, 사람과 에이전트가 같은 파일을 그대로 읽고 쓸 수 있게 하려는 포맷 제안이다.

## 핵심 포인트

- 새로운 지식 서비스가 아니라 지식 교환 포맷 자체를 정의한다.
- 문서 1개가 개념 1개를 표현하고, 파일 경로가 정체성이 된다.
- 구조화 정보는 `YAML frontmatter`, 본문은 일반 Markdown으로 둔다.
- `index.md`와 `log.md` 같은 예약 파일을 선택적으로 둔다.
- 사람, 파이프라인, 에이전트가 같은 규약으로 지식을 생산하고 소비할 수 있게 한다.

## 왜 중요한가

- 사실상 `LLM-wiki` 패턴을 이식 가능하고 상호운용 가능한 형식으로 정리하려는 시도다.
- 위키, 메타데이터 카탈로그, 코드 주석, 런북처럼 흩어진 지식을 하나의 공용 계약으로 묶으려는 방향이다.
- 에이전트 입장에서는 컨텍스트를 매번 새로 조립하는 비용을 줄일 수 있다.
- Git 기반 버전 관리와 잘 맞고, 사람도 읽기 쉽다.

## 한계와 주의점

- Markdown만으로 충분한 영역과 그렇지 않은 영역이 갈린다.
- 스프레드시트, 시각적 관계, 강한 권한이 필요한 지식은 별도 계층이 필요할 수 있다.
- 포맷이 단순한 만큼 팀마다 필드 해석이 달라지면 다시 사일로가 생길 수 있다.
- 표준이 되려면 문법보다 운영 규칙, 검증 도구, 생성/소비 도구가 같이 붙어야 한다.

## AI Labs 토론 질문

- 우리 지식 관리에 OKF 같은 포맷이 실제로 맞는가?
- 현재 `brain/` 구조는 OKF 관점에서 무엇이 이미 준비되어 있고, 무엇을 더 표준화해야 하는가?
- `AGENTS.md`, `index.md`, `raw/wiki` 분리는 어떤 장단점이 있는가?
- 에이전트가 지식을 읽는 것뿐 아니라 갱신까지 맡으려면 어떤 검증 흐름이 필요할까?
- 문서 포맷 표준화가 실제 생산성을 올리는 지점은 어디인가?

## 메모

- 이 글은 새 제품 소개보다, 지식을 에이전트 친화적인 자산으로 다루는 방식에 대한 방향 제시로 보는 편이 맞다.
