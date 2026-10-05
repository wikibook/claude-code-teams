# 결제 서비스

## 명령
- 테스트: pnpm test (커밋 전 반드시 실행)
- 단일 테스트: pnpm test tests/ledger.test.ts
- 테스트 이름으로 실행: pnpm test -t "잔액은 부호를 살려 합산한다"
- 타입 검사: pnpm check (빌드 스텝이 없어 이 검사가 빌드 검증을 대신한다)
- 로컬 실행: pnpm dev (포트 4000, .env.example을 .env로 복사 후)

## 관례
- 패키지 매니저는 pnpm만 쓴다. npm·yarn 금지
- 금액은 항상 정수(원 단위)로 다룬다. 환불은 음수로 기록한다. 부동소수점 금지
- 새 API는 GraphQL(src/graphql/)로 작성한다. src/rest/는 동결 상태로, 버그 수정 외
  변경 금지
- 외부 결제사 호출은 src/gateway/의 클라이언트를 거친다. 직접 HTTP
  호출 금지
- 테스트 유틸리티(describe·it·expect)는 vitest에서 명시적으로 import한다

## 주의
- src/models/ledger.ts의 잔액 계산은 감사 대상 코드다. 수정 전에 반드시
  계획을 세워 승인받을 것
- 테스트에서 실제 결제사 샌드박스를 호출하지 말 것. tests/mocks/의
  createMockGateway를 쓸 것
- 게이트웨이가 얽힌 코드는 GatewayClient를 주입받는 형태로 작성할 것
