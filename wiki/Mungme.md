---
id: ailabs:wiki/mungme
type: Service
title: 멍미
tags: [ai, pet-care, food-safety, data-product, recommendation, public-data]
created: 2026-09-04
status: reviewed
area: ai-labs
relations:
  - type: describes
    target: ailabs:service/mungme
  - type: derived_from
    target: ailabs:raw/2026-09-04-yuil-presentation
  - type: related_to
    target: ailabs:service/dalar
  - type: supports
    target: ailabs:use-case/knowledge-navigation
provenance:
  sources:
    - id: ailabs:raw/2026-09-04-yuil-presentation
      role: presentation-analysis
      captured_at: 2026-09-04
    - url: https://mungme.shop/
      role: canonical-service
      accessed_at: 2026-09-04
---

# 멍미

## 한줄 요약

멍미는 반려동물 보호자가 사료 정보를 읽고 안전성과 적합성을 판단하도록 돕는 데이터 제품이다. 핵심 자산은 생성 모델 자체가 아니라 원천 데이터, 판정 사전, 근거 인용, 추천·가격 정보가 이어지는 운영 파이프라인이다.

## 문제와 사용자

사료 성분표와 리콜 정보를 보호자가 직접 해석하기 어렵고, 정보가 여러 공공기관·제조사 사이트에 흩어져 있다. 멍미는 이 정보와 구매 판단 사이의 간극을 줄이는 것을 목표로 한다.

## 데이터·판정 파이프라인

- 농사로·식약처·농관원·openFDA·제조사 사이트의 데이터를 배치 수집
- 안전·주의·위험 3단계 판정
- 브랜드 식별과 성분 해석에서 LLM 추정보다 사전 기반 판정을 우선
- 추천글 생성 전 품질 필터 적용
- 4개 쇼핑몰 가격 추적과 단종 상품 재연결
- 판정 근거와 원천 링크를 유지해 결과를 검토할 수 있게 설계

발표자료는 성분표 확보율 2.5%→100%, 8,200개 사료 분석, 99% 성분 검증, 340개 원료 사전, 4가지 건강 지표를 제시한다. 이 수치의 표본·산출식·현재성은 별도 검증이 필요하다.

## 재사용 가능한 설계 원칙

멍미에서 중요한 것은 “무엇을 생성했는가”보다 “판정 기준과 원천 데이터가 살아 있는가”다. 리콜차트에 이식된 링크 유실 3중 방어는 데이터 제품에서 수집 실패와 출처 단절을 기본 실패 조건으로 다뤄야 한다는 사례다. 사전은 정답 테이블로, 규칙은 결정론적 코드로 두고 LLM은 보조적인 정리·생성에 제한하는 편이 검증 가능성과 운영 안정성에 유리하다.

## AI Labs 연결

- `Dalar`의 구조화·관계 관리 방식과 결합해 사료·원료·건강 지표·근거 문서를 연결할 수 있다.
- `모두의 개소리`와 리콜·공공데이터 기반 콘텐츠 파이프라인을 공유할 수 있다.
- 멍미에서 검증된 수집 실패 방어, 사전, 골든셋, 출처 인용 방식을 다른 AI Labs 프로젝트의 기본 템플릿으로 확장할 수 있다.

## 검증할 지표

- 원천별 수집 성공률과 최신성
- 성분·브랜드 매칭 정확도 및 골든셋 일치율
- 안전 판정 이의 제기·수정률
- 추천 콘텐츠의 검색 유입과 구매 전환
- 가격·단종 정보의 갱신 지연
