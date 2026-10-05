# 미니숍 (minishop)

가상의 쇼핑몰 백엔드. 주문·쿠폰·환불 도메인을 다룬다.
금액은 원 단위 정수로 계산한다.

## 구조

```
minishop/
  .worktreeinclude        # 워크트리로 복사할 파일 목록
  scripts/
    setup_worktree.sh     # 워크트리 환경 준비 스크립트
    check_imports.py      # 의존성 방향 검사
  src/minishop/
    models.py     # 주문·품목·쿠폰 데이터 모델
    orders.py     # 주문 생성
    pricing.py    # 할인 배분 규칙 (인터페이스 계약의 구현)
    coupons.py    # 쿠폰 적용
    refunds.py    # 부분 환불
  specs/
    pricing-contract.md   # 금액 계산 인터페이스 계약
  tests/
    test_pricing_contract.py  # 계약 테스트
  examples/before_contract/   # 계약 도입 전 구현과 결합 실패 재현
```

## 규칙

- 금액 계산은 반드시 pricing.py를 경유한다. specs/pricing-contract.md가 기준이다.
- 작업 경계와 금지 사항은 CLAUDE.md를 따른다.
- .env, .env.local, tests/fixtures/local_orders.json은 커밋하지 않는다.
  견본은 같은 이름의 .example 파일이다.

## 실행

파이썬 3.10 이상, pytest 7 이상. 저장소 루트(minishop/)에서 실행한다.

```bash
python -m pytest tests/ -v            # 전체 테스트
python scripts/check_imports.py       # 의존성 방향 검사
bash scripts/setup_worktree.sh        # 워크트리 안에서 환경 준비
```
