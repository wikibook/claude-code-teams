# 미니숍 (minishop)

가상의 쇼핑몰 백엔드. 주문·쿠폰·환불 도메인을 다룬다.
금액은 원 단위 정수로 계산한다.

## 구조

```
minishop/
  .claude/
    agents/               # 리뷰어 서브에이전트 3종
    hooks/check_doc_sync.py   # 커밋 시 코드·문서 동기화 확인 훅
  evals/
    cases.json            # 평가 케이스 (골든 케이스)
    fixtures/             # 케이스 입력 diff
    run_evals.py          # 평가 실행 스크립트
  scripts/                # 방향 검사, 워크트리 준비, 계약 테스트 훅
  src/minishop/           # models·orders·pricing·coupons·refunds
  specs/
    pricing-contract.md   # 금액 계산 인터페이스 계약
  tests/
    test_pricing_contract.py  # 계약 테스트
```

## 규칙

- 금액 계산은 반드시 pricing.py를 경유한다. specs/pricing-contract.md가 기준이다.
- 계약 영역 테스트의 기댓값은 계약 문서에서만 가져온다. 구현을 보고 맞추지 않는다.
- 작업 경계와 금지 사항은 CLAUDE.md를 따른다.

## 실행

파이썬 3.10 이상, pytest 7 이상. 저장소 루트(minishop/)에서 실행한다.

```bash
python -m pytest tests/ -v            # 전체 테스트
python scripts/check_imports.py       # 의존성 방향 검사
python evals/run_evals.py             # 자산 평가 세트 실행 (claude CLI 필요)
```
