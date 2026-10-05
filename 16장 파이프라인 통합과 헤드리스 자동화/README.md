# 16장 실습 안내: notihub (파이프라인 통합과 헤드리스 자동화)

notihub 조직의 무인 자동화 파일입니다. spend_this_week.csv와 spend_last_week.csv는
예제 16.1(주간 리포트 논평)의 입력으로, 13장 폴더와 동일한 샘플 데이터입니다.

<br>

## 본문 예제와 파일 대응

- ops/report_comment.sh: 주간 리포트 논평 생성 헤드리스 스크립트 (예제 16.1, 실행은 예제 16.2)
- ops/weekly_cost_report.py, ops/member_team.json: 예제 16.1이 파이프 입력으로 사용하는 13장의 주간 리포트 스크립트와 매핑 파일(13장 폴더와 동일본)
- ops/template_lint.py: SDK 기반 템플릿 검수기 (예제 16.3, 실행은 예제 16.4)
- sample_template_bad.txt: 검수기 재현용 템플릿, 지침 세 가지를 모두 위반(수신 거부 안내 없음, 과장 표현, 자리표시자 형식 혼용)
- sample_template_ok.txt: 검수기 재현용 템플릿, 지침을 지킨 대조군
- .github/workflows/issue-triage.yml: 이슈 분류 워크플로 (예제 16.5)
- .claude/commands/triage-issue.md: 분류 기준 커맨드, 워크플로가 호출합니다 (16.2.1 본문 서술의 구현)
- ops/setup_triage_test.sh: 분류용 라벨 생성과 시험 이슈 생성 (예제 16.6)
- .claude/commands/fix-ci.md: CI 실패 분석·수정 커맨드, 자동 수정 워크플로가 호출합니다 (16.2.2 본문 서술의 구현)
- .github/workflows/ci-auto-fix.yml: CI 실패 자동 수정 워크플로 (예제 16.7)
- .github/workflows/ci.yml: 예제 16.7 시험용 CI, 실패해야 자동 수정 워크플로가 트리거됩니다
- src/sum.js: 예제 16.7 시험용 코드, a - b 라는 의도적 결함이 들어 있습니다
- ops/nightly_migrate.sh: 야간 이관 배치 러너 (예제 16.9)
- targets.txt: 이관 대상 템플릿 목록, 러너가 한 줄씩 읽습니다
- templates/: 이관 대상인 v1 템플릿 세 개와 v2 형식 규칙 문서(SPEC-v2.md)
- tools/lint_template.js: v2 스키마 검사, `npm run lint:template <파일>`
- tools/render_test.js: v2 템플릿의 렌더링 검사, `npm test`
- package.json: 위 두 검사를 npm 스크립트로 등록합니다

<br>

## 실행 방법

- 예제 16.1·16.2: `sh ops/report_comment.sh spend_this_week.csv spend_last_week.csv`
- 예제 16.3·16.4: `pip install claude-agent-sdk anyio` 후 `python ops/template_lint.py sample_template_bad.txt`
- 예제 16.6: `sh ops/setup_triage_test.sh` (라벨 생성과 시험 이슈 생성)
- 예제 16.9: `sh ops/nightly_migrate.sh` (targets.txt와 templates/가 저장소에 포함되어 있습니다)

<br>

## 자격 증명

자격 증명은 무인 실행이므로 환경 변수로 공급합니다. 이 저장소의 스크립트는 모두 `--bare`로 실행되는데, --bare는 장기 토큰 변수(CLAUDE_CODE_OAUTH_TOKEN)를 읽지 않으므로 콘솔 API 키를 ANTHROPIC_API_KEY에 넣어 실행합니다. `claude setup-token`으로 만든 장기 토큰은 GitHub Actions 예제(16.5·16.7)처럼 bare가 아닌 경로에서만 사용합니다. 윈도우에서는 셸 스크립트 예제를 Git Bash나 WSL에서 실행하고, 한글 출력이 깨지면 콘솔 출력 인코딩을 UTF-8로 지정하세요.

<br>

## 깃허브 액션 예제(16.5·16.7)의 시험 절차

예제 16.5·16.7(깃허브 액션)는 로컬 실행이 불가능하므로 시험용 저장소가 필요합니다. 절차는 다음과 같습니다. 저장소에 .github/workflows와 .claude/commands를 함께 커밋하고, 저장소 설정의 Actions 시크릿에 자격 증명을 등록합니다. 콘솔 API 키는 ANTHROPIC_API_KEY 시크릿을 그대로 쓰고, `claude setup-token`으로 만든 장기 토큰은 CLAUDE_CODE_OAUTH_TOKEN 시크릿에 넣은 뒤 액션 입력을 anthropic_api_key 대신 claude_code_oauth_token으로 바꿉니다. 라벨은 워크플로 실행 전에 저장소에 미리 만들어 두어야 하며, area/·type/·p0~p3·needs-info가 대상입니다. 이슈를 열지 않고 반복 시험하려면 워크플로의 on 아래에 workflow_dispatch를 임시로 추가해 Actions 탭에서 수동 실행합니다. 이 추가는 시험용이므로 지면 예제에는 포함하지 않았습니다.

저장소에 처음 반영할 때는 순서를 지켜 주세요. 파일을 모두 커밋해도 곧바로 실행되는 워크플로는 없도록 트리거를 제한해 두었지만, 시험을 시작하기 전에 자격 증명과 저장소 설정을 먼저 갖춰야 합니다. 순서는 다음과 같습니다. 먼저 전체 파일을 기본 브랜치에 커밋합니다. 다음으로 Actions 시크릿에 CLAUDE_CODE_OAUTH_TOKEN을 등록하고, Settings > Actions > General에서 "Allow GitHub Actions to create and approve pull requests"를 켭니다. 라벨 부여와 브랜치 푸시에 필요한 쓰기 권한은 워크플로의 permissions 선언으로 부여되므로 Workflow permissions 기본값은 바꾸지 않아도 됩니다. 자동 수정 워크플로의 허용 목록은 claude/fix- 접두사의 브랜치로 푸시를 제한하지만 접두사 검사만으로는 기본 브랜치 직접 반영을 막을 수 없으므로, 9.3.3과 같이 기본 브랜치에 "Require a pull request before merging" 룰셋을 함께 적용해 주세요. 그다음 `sh ops/setup_triage_test.sh`로 라벨과 시험 이슈를 만들어 분류 파이프라인을 확인합니다. 마지막으로 자동 수정을 시험합니다.

지면 예제인 issue-triage.yml과 ci-auto-fix.yml은 인증 입력이 ANTHROPIC_API_KEY 시크릿이므로, 콘솔 키 없이 `claude setup-token`의 장기 토큰만 사용한다면 그대로는 인증에 실패합니다. 장기 토큰으로 직접 돌리려면 아래와 같이 고칩니다.

issue-triage.yml에서 고칠 곳은 한 줄입니다.

```yaml
# 변경 전
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
# 변경 후
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
```

ci-auto-fix.yml도 고칠 곳은 같은 한 줄입니다. anthropic_api_key 입력을 위와 동일하게
claude_code_oauth_token으로 바꾸면 됩니다. PR 생성에 필요한 나머지 요소는 파일에 이미
포함되어 있습니다. 자동 수정 PR의 CI 실패가 다시 자동 수정을 부르는 연쇄는 트리거 조건의
head_branch 검사(claude/fix- 제외)가 막고, 브랜치 푸시와 PR 생성 권한은 permissions
블록(contents·pull-requests 쓰기)이, PR 생성과 실행 로그 조회는 github_token 입력이
담당합니다. 허용 목록의 `Bash(npm test:*)`는 이 저장소의 검증 명령에 맞춘 것이므로
프로젝트의 테스트 명령에 맞게 조정하세요.

예제 16.7의 시험 절차는 다음과 같습니다. 준비가 끝난 뒤 demo/ 로 시작하는 브랜치를 만들어 푸시하면 CI가 실행되어 실패하고, 자동 수정 워크플로가 이어서 실행됩니다. 정상 동작하면 claude/fix-로 시작하는 브랜치와 PR이 생성되고, src/sum.js의 a - b가 a + b로 수정되어 있습니다. 테스트 쪽이 수정되었다면 fix-ci 커맨드의 금지 조항이 작동하지 않은 것이므로 커맨드를 보강합니다.

예제 16.9의 시험 절차는 다음과 같습니다. 러너는 jq를 사용하므로 실행 전에 jq가 설치되어 있어야 합니다. 자격 증명은 예제 16.1과 동일하게 환경 변수로 공급합니다. 준비가 끝나면 저장소 루트에서 `sh ops/nightly_migrate.sh`를 실행합니다. 러너는 targets.txt의 템플릿을 한 줄씩 읽어 파일 하나에 헤드리스 실행 하나를 배정하고, 성공한 파일은 done.txt에, 실패한 파일은 failed.txt에 기록합니다. 실행이 끝나면 templates/의 파일이 v2 형식으로 바뀌었는지, done.txt에 세 파일이 모두 기록되었는지 확인합니다.

이 구성에서 확인할 지점이 두 가지 있습니다. 하나는 `--bare`가 지침 파일의 자동 로드를 생략하므로 세션이 v2 형식을 미리 알지 못한다는 점입니다. 세션은 스키마 검사의 오류 메시지를 통해 templates/SPEC-v2.md를 찾아 읽고 규칙을 파악합니다. 검증 도구의 오류 메시지가 곧 세션의 지침이 되는 구조입니다. 다른 하나는 중단 조건입니다. 연속 실패가 세 번 발생하면 러너가 종료하므로, 이를 확인하려면 형식을 맞출 수 없는 파일을 templates/에 추가하고 targets.txt 앞쪽에 배치합니다.

다시 실행할 때는 done.txt와 failed.txt를 지우고 templates/를 원래 상태로 되돌립니다. 러너는 done.txt에 기록된 파일을 건너뛰므로, 파일을 지우지 않으면 두 번째 실행에서 아무 작업도 수행하지 않습니다.
