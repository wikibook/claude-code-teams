# 7장 실습 안내: notihub

7장의 예제 저장소입니다. 사내 알림 서비스 모노레포로, 파일럿을 마친 팀이 공통
CLAUDE.md·설정·권한 정책·훅 가드레일을 얹는 무대입니다. 이 폴더의 notihub는
7장을 완주한 상태의 스냅샷입니다. 8장 실습은 「08장 노하우의 조직 자산화」
폴더의 notihub(8장 완주 상태)를 사용합니다.

<br>

## 준비

- Node.js와 pnpm이 필요합니다(훅의 커밋 전 검사가 `pnpm -r check`를 호출합니다).
- 루트에서 `pnpm install`을 먼저 실행합니다(typescript·vitest 등 개발 의존성 설치).
- Python 3이 필요합니다(훅 스크립트 실행).
- 저장소를 처음 열면 워크스페이스 신뢰를 수락해야 프로젝트 설정의
  허용 규칙과 훅이 적용됩니다 (7.2.1).

<br>

## 본문 예제와 파일 대응

- CLAUDE.md: 예제 7.1 (팀 공통 CLAUDE.md)
- .claude/settings.json: 예제 7.2/7.4/7.7/7.8 (권한 규칙·훅 등록·표기)
- ops/managed-settings.json: 예제 7.3 (조직 관리 설정. 실제 배포 위치는 운영체제별
  시스템 디렉터리이며, 표 7.4의 경로를 따릅니다. 저장소 안의 이 파일은 읽히지 않습니다)
- docs/policies/permissions.md: 예제 7.5 (권한 정책 문서)
- .claude/hooks/guard_commands.py: 예제 7.6 (위험 명령 차단 훅)
- .claude/hooks/verify_before_commit.py: 예제 7.9 (커밋 전 검증 훅)
- .claude/hooks/format_changed.py: 수정 직후 포맷 훅 (예제 7.8에서 등록)
- CODEOWNERS: 예제 7.10 (표준 소유자 지정)
- .github/PULL_REQUEST_TEMPLATE/standards.md: 예제 7.11 (표준 수정 PR 템플릿)
- specs/delivery-contract.md: 발송 계약 (7.1.1에서 경로 참조)

<br>

## 훅 단독 검증 (7.4.1)

세션 없이 이벤트 JSON을 표준 입력으로 넣어 차단 훅을 검증할 수 있습니다.

```bash
echo '{"tool_input":{"command":"git push --force origin main"}}' \
  | python .claude/hooks/guard_commands.py
# 종료 코드 2와 차단 메시지가 나오면 정상
```

<br>

## 참고

- 팀 도구(본문에서 언급): .claude/commands/review.md·commit.md
- 저장소 골격: package.json, pnpm-workspace.yaml, services/*, packages/shared
