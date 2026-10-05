# 8장 실습 안내: notihub + claude-plugins

8장의 예제 저장소입니다. notihub는 사내 알림 서비스 모노레포로, 7장의 팀 공통
환경 위에 노하우 자산화(스킬 승격, 온보딩 문서)를 얹은 8장 완주 스냅샷입니다.
claude-plugins는 notihub-kit 플러그인을 담은 사내 마켓플레이스 저장소입니다(8.2.2).
7장 실습은 「07장 팀 공통 환경 구축」 폴더의 notihub(7장 완주 상태)를 사용합니다.

<br>

## 준비

- Node.js와 pnpm이 필요합니다. notihub 루트에서 `pnpm install`을 먼저 실행합니다(typescript·vitest 등 개발 의존성 설치).
- 나머지 준비(Python, 워크스페이스 신뢰)는 7장 폴더 README의 준비 절과 같습니다.

<br>

## 본문 예제와 파일 대응

notihub/
- .claude/skills/dispatch-review/SKILL.md: 예제 8.1 (발송 경로 리뷰 스킬)
- docs/onboarding.md: 예제 8.4 (온보딩 안내 문서)
- 7장에서 만든 파일(CLAUDE.md, .claude/settings.json, hooks/, docs/policies/,
  CODEOWNERS, PR 템플릿 등)은 그대로 유지됩니다. 목록은 7장 폴더의 README를 참조하세요.

claude-plugins/
- .claude-plugin/marketplace.json: 예제 8.3 (사내 마켓플레이스 카탈로그)
- plugins/notihub-kit/.claude-plugin/plugin.json: 예제 8.2 (플러그인 매니페스트)
- plugins/notihub-kit/skills/: commit·review·log-research 스킬
- plugins/notihub-kit/CHANGELOG.md: 버전별 변경 기록(8.2.1)

<br>

## 마켓플레이스 실습 (8.2.2)

로컬 경로로 마켓플레이스를 등록해 설치 흐름을 재현할 수 있습니다.

```
/plugin marketplace add ./claude-plugins
/plugin install notihub-kit@notihub-plugins
```

설치 후 /notihub-kit:review처럼 플러그인 네임스페이스로 스킬을 호출합니다.
본문 예시의 notihub/claude-plugins 주소는 사내 Git 호스팅을 전제로 한 것입니다.

<br>

## 온보딩 실습 (8.3)

docs/onboarding.md의 순서를 따릅니다. 탐색 세션 프롬프트는 본문 8.3.1의
사용자 입력을 그대로 사용할 수 있습니다.
