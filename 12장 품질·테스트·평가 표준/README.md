# 12장 실습 안내: minishop

12장의 예제 저장소입니다. 11장까지의 minishop에 품질·평가 체계(문서 동기화 훅,
평가 세트)가 더해진 스냅샷입니다. 이전 상태는 「09장」~「11장」 폴더의
minishop을 사용합니다.

<br>

## 본문 예제와 파일 대응

- .claude/hooks/check_doc_sync.py: 예제 12.1 (문서 동기화 확인 훅,
  PreToolUse의 permissionDecision: ask)
- evals/cases.json: 예제 12.2 (평가 케이스 파일)
- evals/run_evals.py: 예제 12.3 (평가 실행 스크립트 발췌)
- 예제 12.4: 평가 세트 실행 명령(아래 실행 참조)
- evals/fixtures/: 케이스 입력 diff 3종
  (c01 정가 기준 적립 위반, c02 정상 리팩터링, c03 테스트가 구현을 복제)

<br>

## 훅 실습 (12.2.2)

계약 인접 코드(src/minishop/pricing.py 등)만 수정하고 specs/를 건드리지
않은 채 세션에 커밋을 지시하면, 본문 12.2.2의 세션 표기처럼 확인 창이
나타납니다. 훅 단독 검증도 가능합니다.

```bash
git add src/minishop/pricing.py
echo '{"tool_input":{"command":"git commit -m test"}}' \
  | python .claude/hooks/check_doc_sync.py
# permissionDecision: ask JSON이 출력되면 정상
```

<br>

## 평가 실습 (12.3)

claude CLI가 설치·인증된 환경에서 실행합니다. 케이스마다 비대화형 세션이
하나씩 실행되므로 사용량이 발생합니다.

```bash
python evals/run_evals.py
# 기대 출력: 3/3 통과
```

케이스를 추가할 때는 위반 없는 입력을 절반 수준으로 유지하고(12.3.1),
표현이 변할 수 있는 문자열 대신 고정 문구·식별자를 expect에 씁니다.
