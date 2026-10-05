# 미니숍 (minishop)

가상의 쇼핑몰 백엔드. 주문·쿠폰·환불 도메인을 다룬다.
금액은 원 단위 정수로 계산한다.

## 구조

```
minishop/
  .github/workflows/
    ci.yml                # 병합 게이트 (계약 테스트·명세 동반 확인)
    claude-review.yml     # PR 자동 1차 리뷰 워크플로
  .claude/agents/
    contract-reviewer.md  # 계약 리뷰어
    security-reviewer.md  # 보안 리뷰어
    convention-reviewer.md # 컨벤션 리뷰어
  .worktreeinclude        # 워크트리로 복사할 파일 목록
  scripts/
    setup_worktree.sh     # 워크트리 환경 준비 스크립트
    check_imports.py      # 의존성 방향 검사
  src/minishop/           # models·orders·pricing·coupons·refunds
  specs/
    pricing-contract.md   # 금액 계산 인터페이스 계약
  tests/
    test_pricing_contract.py  # 계약 테스트
  examples/before_contract/   # 계약 도입 전 구현과 결합 실패 재현
```

## 규칙

- 금액 계산은 반드시 pricing.py를 경유한다. specs/pricing-contract.md가 기준이다.
- 작업 경계와 금지 사항은 CLAUDE.md를 따른다.
- 발송·금액 코드의 리뷰에는 contract-reviewer를 사용한다.

## 실행

파이썬 3.10 이상, pytest 7 이상. 저장소 루트(minishop/)에서 실행한다.

```bash
python -m pytest tests/ -v            # 전체 테스트
python scripts/check_imports.py       # 의존성 방향 검사
```
