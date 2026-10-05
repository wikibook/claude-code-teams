---
description: 결제 코드 변경분 리뷰
argument-hint: [파일 경로 또는 비워 두면 전체 변경분]
allowed-tools: Read, Grep, Glob, Bash(git diff:*)
---

## 변경 내역

!`git diff HEAD --stat`

## 요청

$ARGUMENTS 를 중심으로 변경분을 리뷰한다. 인자가 없으면 전체 변경분을 대상으로 한다. 다음 순서를 지킨다.

1. 금액 계산 경로: 부동소수점 사용, 환불 부호 처리를 먼저 확인한다
2. 관례 위반: packages/api/CLAUDE.md의 관례 절과 대조한다
3. 테스트 공백: 변경 코드가 다루는 에지 케이스 중 테스트가 없는 것을 지적한다

발견 항목은 심각도(높음·중간·낮음)로 나눠 보고한다.
