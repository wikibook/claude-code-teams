packages/ 아래 세 패키지로 구성된 모노레포다.

- packages/api: 결제 API 서버 (TypeScript, GraphQL·REST)
- packages/web: React 프런트엔드 (Vite, TypeScript)
- packages/shared: 양쪽이 쓰는 공용 TypeScript 유틸리티

명령은 모노레포 루트가 아니라 각 패키지 디렉터리에서 실행한다.
패키지마다 tsconfig.json, package.json, 테스트 스위트가 따로 있다.
