# 11장 실습 안내: minishop

11장의 예제 저장소입니다. 10장까지의 minishop에 PR 자동 리뷰 워크플로와
리뷰어 서브에이전트 3종이 더해진 스냅샷입니다. 이전 상태는
「09장 작업 결합의 공학」·「10장 Git 전략과 병렬 작업」의 minishop을 사용합니다.

<br>

## 준비

- GitHub 저장소로 올려야 파이프라인 실습이 가능합니다(공개 저장소 권장.
  포크 PR에는 시크릿이 전달되지 않고, 무료 프라이빗에서는 룰셋이 강제되지 않습니다).
- 클로드 코드 세션에서 /install-github-app을 실행합니다(gh 인증에 workflow 스코프가 필요합니다.
  없으면 `gh auth refresh -h github.com -s repo,workflow`).
- 인증 시크릿: 콘솔 API 키(ANTHROPIC_API_KEY) 또는
  `claude setup-token`으로 만든 장기 토큰(CLAUDE_CODE_OAUTH_TOKEN) 중 하나를 등록합니다.

<br>

## 본문 예제와 파일 대응

- .github/workflows/claude-review.yml: 예제 11.1 (PR 자동 리뷰 워크플로)
- .claude/agents/contract-reviewer.md: 예제 11.2 (계약 리뷰어 서브에이전트)
- .claude/agents/security-reviewer.md, convention-reviewer.md: 표 11.4의 나머지 두 리뷰어(본문 발췌 없음)
- 9~10장에서 만든 파일(계약·게이트·워크트리 재료)은 그대로 유지됩니다.

<br>

## 파이프라인 실습 (11.2.1)

1. 계약을 위반하는 변경(예: 적립액을 정가 기준으로 계산)을 담은 PR을 올립니다.
2. Claude Review 워크플로가 실행되어 위반 줄에 인라인 코멘트(그림 11.3),
   최상위에 심각도 요약 코멘트(그림 11.4)가 달리는지 확인합니다.
3. 기준액을 paid_total로 고쳐 푸시하면 재리뷰에서 발견 없이 통과합니다.
4. 트리거에서 synchronize를 빼면 PR 생성 시 1회만 리뷰합니다(사용량 조절).

<br>

## 로컬 리뷰어 실습 (11.2.2)

세션에서 발송·금액 변경 후 "contract-reviewer로 검토해줘"라고 요청하면
저장소의 정의 파일 기준으로 독립 컨텍스트 리뷰가 실행됩니다.
