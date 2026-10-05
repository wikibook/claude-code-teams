# 미니숍 프로젝트 규칙

주문·쿠폰·환불을 다루는 쇼핑몰 백엔드다. 금액은 원 단위 정수로 계산한다.

## 작업 경계
- 금액 계산은 반드시 pricing.py를 경유한다.
  specs/pricing-contract.md가 기준이다.
- coupons.py와 refunds.py는 서로 import하지 않는다.
- models.py와 pricing.py는 직접 수정하지 않는다.
  변경이 필요하면 수정안을 제시하고 승인을 기다린다.
- 새 기능 모듈은 기능 계층에 만들고, 공유가 필요해지면
  공유 계층으로 올리는 제안을 먼저 한다.

## 작업 방법
- 작업과 관련된 계약이 있는지 specs/의 목록을 먼저 확인한다.
- 구현 후 python -m pytest tests/ 를 실행해 전체 테스트를 확인한다.
- 의존성 방향은 python scripts/check_imports.py 로 검사한다.
