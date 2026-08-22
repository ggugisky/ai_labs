---
id: ailabs:wiki/lampas
type: Service
tags: [ai, generative-ai, image, video, workflow, productization]
created: 2026-08-22
status: reviewed
area: ai-labs
relations:
  - type: discussed_in
    target: ailabs:raw/meeting/20260807
  - type: describes
    target: ailabs:service/lampas
provenance:
  sources:
    - id: ailabs:raw/meeting/20260807
      role: meeting
      captured_at: 2026-08-07
    - url: https://models.lampas.io/
      role: official
      accessed_at: 2026-08-22
---

# Lampas

> Source: [Lampas](https://www.lampas.io/), [Lampas Models](https://models.lampas.io/), [Lampas SDK](https://sdk.lampas.io/)
> Meeting: [[raw/meeting/20260807]]

## 한줄 요약

Lampas는 이미지·영상 생성 모델과 편집 단계를 조합해 콘텐츠 제작 파이프라인을 실험하고, 검증된 조합을 서비스로 만들 수 있게 하는 생성형 미디어 플랫폼이다.

## 미팅에서 확인한 핵심

- 이미지, 비디오, 편집 단계를 노드 또는 파이프라인으로 연결한다.
- 여러 모델을 직접 조합해 결과가 좋은 흐름을 실험한다.
- 잘 동작하는 조합을 반복 가능한 앱이나 상품으로 전환한다.
- 브랜드·상품·공간을 입력으로 받아 콘텐츠 제작 파이프라인을 만든다.
- 크레딧과 결제를 연결해 사용량 기반 서비스로 운영할 수 있다.

## 현재 서비스 구조

공식 모델 카탈로그는 Lampas AI Gateway를 통해 이미지·비디오·텍스트·오디오 모델을 한 곳에서 실행하는 형태를 보여준다. 이미지 생성·편집, image-to-video, text-to-video, reference-to-video 등 다양한 작업을 모델별로 선택할 수 있다.

SDK 소개에는 actor를 만들고 선택한 뒤 preset과 transform을 적용해 이미지를 만드는 흐름이 제시되어 있다. 이는 단발성 프롬프트보다 `재사용 가능한 주체와 변환 파이프라인`을 중심에 두는 설계다.

## 제품화 흐름

1. 브랜드·상품·공간 같은 입력을 정의한다.
2. 이미지·영상 모델과 편집 단계를 조합한다.
3. 결과물의 품질·비용·처리 시간을 비교한다.
4. 잘 되는 조합을 preset 또는 앱 기능으로 고정한다.
5. 크레딧·결제·사용량 제한을 붙여 상용 서비스로 운영한다.

## 장점

- 여러 생성 모델을 한 작업 흐름에서 비교할 수 있다.
- 실험 단계와 상용 기능 사이의 간극을 줄인다.
- actor·preset·transform을 통해 반복 제작에 적합한 구조를 만든다.
- 하네스가 서비스로 전환되는 과정을 구체적으로 보여준다.

## 한계와 주의점

- 모델 수가 많아질수록 품질·가격·지연시간을 비교할 운영 기준이 필요하다.
- 모델 제공자의 정책·가격·출력 권리가 바뀌면 파이프라인 안정성이 흔들릴 수 있다.
- 단순히 모델을 많이 연결하는 것만으로는 좋은 콘텐츠가 보장되지 않는다.
- 상용화에는 재현 가능한 preset, 실패 처리, 결과 검수, 비용 상한이 필요하다.

## AI Labs 시사점

Lampas는 `모델을 직접 만드는 것`보다 `여러 모델을 조합해 목적별 생산 파이프라인을 상품화하는 것`에 초점을 둔 사례다. 성환님의 콘텐츠 자동화 하네스와 결합하면 시장 조사와 콘텐츠 형식 분석을 앞단에 두고, Lampas식 생성·편집 pipeline을 뒷단에 붙이는 구조를 생각할 수 있다.
