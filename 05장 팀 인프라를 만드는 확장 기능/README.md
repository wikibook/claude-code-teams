# 5장 실습 안내

5장 「팀 인프라를 만드는 확장 기능」의 실습 폴더입니다. 저장소는 `paylog` 하나이며,
4장 시작 상태의 코드에 4장 지침 파일과 5장의 확장 재료가 모두 얹힌 **5장 완주
시점의 전체 스냅샷**입니다. 본문 캡션 경로(paylog/...)와 그대로 일치합니다.

<br>

## 5장에서 만든 파일 (본문 예제와 문자 단위 일치)

- `.claude/commands/review.md`: 예제 5.1 (리뷰 커맨드)
- `.claude/commands/commit.md`: 예제 5.2 (커밋 커맨드)
- `.claude/settings.json`: 예제 5.3 (훅 등록)
- `.claude/hooks/protect_env.py`: 예제 5.4 (.env 보호 훅)
- `.claude/hooks/propose_memory.py`: 예제 5.5 (CLAUDE.md 갱신 제안 훅)
- `.claude/agents/reviewer.md`: 예제 5.6 (리뷰어 서브에이전트)
- `.claude/skills/gateway-check/`: 예제 5.7 (연동 점검 스킬, checklist.md·decisions.md 동봉)
- `.mcp.json`: 예제 5.11 (Jira MCP 연결)

예제 5.8(플러그인 구성 트리)과 5.9(자동 제안 설정)는 가상의 payteam-kit 구조
예시라 실파일이 없고, 예제 5.10은 연결 명령입니다.

<br>

## 실습 방법

1. 저장소 루트에서 세션을 시작합니다(확장 재료가 루트 .claude/에 있으므로).
2. `/review`, `/commit`으로 커맨드를 실행해 봅니다.
3. `.env` 파일 수정을 지시해 보호 훅(예제 5.4)이 차단하는 것을 확인합니다.
4. `@agent-reviewer 변경분을 리뷰해 줘`로 서브에이전트 위임을 확인합니다.
5. `/mcp`로 Jira 서버 연결 상태를 확인합니다(사용하려면 승인과 OAuth 로그인이 필요합니다).

<br>

## 유의점

- 훅 스크립트는 파이썬으로 실행되므로 python이 PATH에 있어야 합니다.
- 훅의 동작을 실습하는 세션에서 .env 수정이 차단되는 것은 정상입니다(정책 메시지가
  표시됩니다). 훅을 끄려면 `.claude/settings.json`의 등록을 제거하세요.
- 4장을 이 폴더에서 실습하지 않습니다. 4장은 지침이 없는 시작 상태(4장 폴더의
  paylog)에서 시작해야 재현됩니다.
