# 알림 API

담당: @notihub/api-owners (발송 도메인 문의)

## 명령
- 테스트: pnpm test
- 단일 테스트: pnpm test tests/dispatch.test.ts
- 타입 검사: pnpm check
- 로컬 실행: pnpm dev (포트 4100, .env.example을 .env로 복사 후)

## 관례
- 패키지 매니저는 pnpm만 쓴다
- 발송은 반드시 src/dispatch/의 파이프라인을 거친다. 채널 클라이언트 직접 호출 금지
- 알림 본문은 packages/shared의 템플릿 엔진으로만 만든다. 문자열 조립 금지
- 테스트에서 실제 채널을 호출하지 말 것. tests/mocks/의 createMockChannel을 쓸 것

## 주의
- src/dispatch/의 변경은 계획 검토가 의무다 (docs/policies/permissions.md)
- 중복 제거 키의 변경은 specs/delivery-contract.md의 갱신이 선행되어야 한다
