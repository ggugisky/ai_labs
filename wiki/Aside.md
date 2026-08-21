---
tags: [ai, agent, browser, computer-use, privacy, automation]
created: 2026-08-21
status: reviewed
area: ai-labs
---

# Aside

> Source: [Aside official site](https://aside.com/)
> Meeting: [[raw/meeting/20260821]]

## 한줄 요약

Aside는 로그인된 웹사이트와 로컬 파일을 직접 다루는 브라우저 중심 AI assistant이며, 로컬 memory·비밀번호 보호·민감 작업 승인·접근 로그를 결합한 computer-use 제품이다.

## 핵심 기능

- 브라우저 안에서 자연어로 작업 요청
- Gmail, Figma, WhatsApp, Vercel 등 로그인된 웹 서비스 사용
- 메시지, 댓글, 후속 연락, 내부 도구 업무 수행
- 로컬 컴퓨터의 문서·스프레드시트 작업
- 브라우징 기록과 업무 맥락을 memory로 활용
- ChatGPT·Claude 구독 또는 자체 API key 사용
- 여러 agent tab을 통해 병렬 작업

## 보안 설계

- 비밀번호를 AI 모델에 노출하지 않고 autofill로 로그인
- 결제·게시·메시지 같은 민감한 행동은 human approval 대기
- credential 사용 기록과 접근 범위 확인
- 로컬 우선 memory와 데이터 처리
- Secure Enclave, 암호화, 파일·네트워크 sandbox를 표방

## Grok Bot과의 비교

- Grok Bot: 여러 Bot이 역할을 나눠 장기·병렬 업무를 수행하는 팀형 포지셔닝
- Aside: 브라우저와 계정, 비밀번호, 승인·감사 흐름을 한 제품 안에 묶은 안전한 computer-use 포지셔닝

둘 다 API 연동이 어려운 웹 업무를 직접 수행한다는 공통점이 있지만, Aside는 특히 credential 보호와 human-in-the-loop 경계를 전면에 내세운다.

## 장점

- API가 없는 웹 서비스도 사람의 브라우저 흐름으로 자동화할 수 있다.
- 계정 비밀번호를 모델에게 직접 전달하지 않는 구조를 지향한다.
- 민감 작업의 승인과 credential 접근 로그가 명확하다.
- 기존 브라우징 맥락과 업무 데이터를 활용해 반복 설명을 줄일 수 있다.

## 한계와 주의점

- 브라우저 자동화는 웹 UI 변경과 세션 만료에 취약하다.
- 로그인된 계정의 권한 범위가 곧 에이전트의 실행 범위가 된다.
- 로컬 처리·암호화·benchmark 수치는 제품의 공식 설명이므로 실제 도입 전 기술·법무 검증이 필요하다.
- 결제, 게시, 고객 응대 같은 작업은 자동화보다 승인 정책과 취소·복구 절차가 먼저다.

## AI Labs 시사점

Aside는 AI 에이전트에서 보안이 단순한 prompt 정책이 아니라 credential vault, scoped access, approval, audit log의 조합이라는 점을 잘 보여준다. 외부 서비스 연동을 다루는 Margaret Gateway의 approval/HITL 설계와 비교하기 좋은 사례다.

