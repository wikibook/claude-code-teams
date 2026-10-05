---
description: 관례에 맞는 커밋 생성
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(pnpm -r check:*)
disable-model-invocation: true
---

## 현재 상태

!`git status --short`

## 절차

1. 변경 파일을 논리 단위로 묶는다. 서로 다른 관심사가 섞여 있으면
   커밋을 나눈다
2. 커밋 메시지는 한국어로 쓴다. 첫 줄은 "영역: 변경 요약" 형식이다
   (예: api: 재시도 간격 상한 추가)
3. pnpm -r check가 통과하는지 먼저 확인하고, 실패하면 커밋하지 않고 보고한다
