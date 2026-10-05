---
name: gateway-check
description: 외부 결제사 연동 코드의 점검 절차. gateway 클라이언트를
  추가·수정하거나 연동 장애를 조사할 때 사용한다.
---

# 결제사 연동 점검

## 점검 순서

1. 모든 외부 호출이 src/gateway/의 클라이언트를 거치는지 확인한다.
   직접 HTTP 호출이 발견되면 위반으로 보고한다
2. 타임아웃과 재시도 정책이 명시돼 있는지 확인한다. 재시도는
   멱등 요청에만 허용된다
3. 테스트가 tests/mocks/의 createMockGateway를 쓰는지 확인한다.
   실제 샌드박스 호출은 금지다
4. 오류 응답의 계약은 checklist.md의 표와 대조한다

## 참고 파일

- 세부 점검표: checklist.md
- 재시도 정책의 결정 배경: decisions.md
