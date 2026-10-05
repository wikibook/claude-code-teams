# notihub

사내 알림 서비스 모노레포. 각 팀의 시스템에서 이벤트를 받아
슬랙·이메일·웹훅 채널로 알림을 발송한다.

## 구조
- services/api — 알림 API와 발송 파이프라인. 발송 로직의 진실 원천
- services/web — 관리 콘솔 (React)
- packages/shared — 공용 타입과 알림 템플릿 엔진

## 명령
- 명령은 각 작업 공간 디렉터리에서 실행한다 (예: services/api에서 pnpm test)
- 전체 타입 검사는 루트에서 pnpm -r check (커밋 전 훅이 자동 실행)

## 계약
- 발송 규칙(재시도·중복 제거)을 다루는 코드는 specs/delivery-contract.md를 따른다
- 발송 파이프라인의 세부 관례는 services/api/CLAUDE.md를 따른다

## 작업 규약
- 커밋 첫 줄은 "영역: 변경 요약" 형식 (예: api: 재시도 간격 상한 추가)
- 리뷰는 /notihub-kit:review, 커밋은 /notihub-kit:commit을 사용한다
- 계획 검토가 의무인 작업 유형은 docs/policies/permissions.md를 따른다

## 금지
- 운영 발송 채널 호출 금지 (훅으로 차단됨) — 테스트는 샌드박스 채널 사용
- .env 계열 파일은 읽지 않는다 (권한 규칙으로 차단됨)
