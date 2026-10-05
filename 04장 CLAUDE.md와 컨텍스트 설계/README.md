# 4장 실습 안내

4장 「CLAUDE.md와 컨텍스트 설계」의 실습 폴더입니다. 구성은 두 가지입니다.

- `paylog`: 실습 시작 상태의 저장소입니다. 결제 서비스 모노레포(packages/api·web·shared)로,
  **의도적으로 CLAUDE.md·README·규칙 파일이 없습니다**. 4.1.1의 /init 세션이 "기존
  CLAUDE.md, README, Cursor/Copilot 규칙은 없어서"를 전제로 하므로 지침 파일을
  미리 만들지 않습니다.
- `paylog-complete`: 4장을 완주한 상태의 지침 파일 모음(정답 대조용)입니다. 각 파일은
  paylog의 같은 경로에 놓였을 때의 완성본입니다.
  - `CLAUDE.md`: 예제 4.5 (모노레포 루트)
  - `packages/api/CLAUDE.md`: 예제 4.2 (결제 API 패키지)
  - `packages/api/.claude/rules/api-design.md`: 예제 4.4 (경로 스코프 규칙)
  - `.claude/settings.local.json`: 예제 4.6 (claudeMdExcludes)

<br>

## 준비

1. Node.js 20 이상과 pnpm이 필요합니다. `paylog/packages/api`에서 의존성을 설치하고
   테스트가 통과하는지 확인합니다.

   ```
   cd paylog/packages/api
   pnpm install
   pnpm test
   ```

2. 실습은 `packages/api` 디렉터리에서 세션을 열어 시작합니다(4.1.1의 /init).

<br>

## 본문에서 사용하는 곳

- 4.1.1: packages/api에서 /init으로 초안 생성, 오토 메모리와의 역할 구분
- 4.1.2: 나쁜 파일(예제 4.1)과 좋은 파일(예제 4.2)의 대비, 수수료 기능 세션
- 4.2.1: 계층 배치, 임포트(예제 4.3), 경로 스코프 규칙(예제 4.4)
- 4.2.2: 루트 CLAUDE.md(예제 4.5), claudeMdExcludes(예제 4.6)
- 4.3.1: /context all로 토큰 측정, /doctor로 다이어트 제안

<br>

## 유의점

- 실습 결과로 만들어지는 지침 파일은 paylog-complete와 대조해 확인합니다. 예제 4.2·
  4.4·4.5·4.6은 paylog-complete의 실파일과 문자 단위로 일치합니다.
- paylog에 지침 파일을 만든 상태에서 처음부터 다시 실습하려면 생성한
  CLAUDE.md·.claude/ 파일들을 삭제하면 됩니다(코드는 바뀌지 않습니다).
