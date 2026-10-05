# 10장 실습 안내: minishop

10장의 예제 저장소입니다. 9장 완주 상태의 minishop에 워크트리 병렬 운영
재료(.worktreeinclude, setup_worktree.sh, 로컬 전용 파일 견본)가 더해진
스냅샷입니다. 9장까지의 상태는 「09장 작업 결합의 공학」의 minishop을,
11장 이후는 각 장 폴더의 minishop을 사용합니다.

<br>

## 준비

- 파이썬 3.10 이상, pytest 7 이상이 필요합니다. 실행은 저장소 루트(minishop/)에서 합니다.
- `.worktreeinclude`의 복사 대상은 커밋되지 않는 로컬 파일이므로
  견본에서 먼저 만들어 둡니다.

```bash
cp .env.example .env
cp .env.local.example .env.local
cp tests/fixtures/local_orders.example.json tests/fixtures/local_orders.json
```

<br>

## 본문 예제와 파일 대응

- .worktreeinclude: 예제 10.1 (워크트리로 복사할 파일 목록)
- scripts/setup_worktree.sh: 예제 10.2 (워크트리 환경 준비 스크립트)
- 예제 10.3(근거가 포함된 커밋 메시지)은 메시지 예시로 실파일이 없습니다.
- 9장에서 만든 파일(계약·게이트·오너십 등)은 그대로 유지됩니다. 목록은
  9장 폴더의 README를 참조하세요.

<br>

## 워크트리 실습 (10.2)

터미널 두 개에서 각각 세션을 시작하고, 다른 창에서 목록을 확인합니다.

```bash
claude --worktree coupon    # 첫 번째 터미널
claude --worktree points    # 두 번째 터미널

git worktree list
```

워크트리 안에서 `sh scripts/setup_worktree.sh`를 실행하면 가상 환경과
의존성이 준비되고, 계약 테스트가 한 번 실행되어 환경이 실제로 동작하는지
확인됩니다. 윈도우에서는 Git Bash로 실행합니다(PowerShell의 `bash`는 WSL을
가리킵니다). 본문 10.2.2의 정리 절차(git worktree remove, 잠금 해제)도 이
저장소에서 그대로 재현할 수 있습니다.
