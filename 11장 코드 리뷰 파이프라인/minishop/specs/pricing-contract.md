# 금액 계산 인터페이스 계약

- 버전: 1.0
- 오너: 결제 도메인 (@payments-team)
- 상태: 승인됨
- 마지막 수정: 2026-07-06

## 결정

1. 주문 수준 할인(쿠폰 등)은 반드시 품목 단위로 배분한다.
   배분 결과는 각 품목의 `paid_amount`에 저장한다.
2. 배분 규칙: 품목 정가 비율대로 나누고, 반올림 잔차는
   금액이 큰 품목부터 1원씩 흡수한다(큰 금액 우선 배분).
3. 불변식: 모든 품목 `paid_amount`의 합 == 주문 `paid_total`.
   1원의 누수도 허용하지 않는다.
4. 환불·정산·영수증 등 금액을 다루는 모든 코드는
   품목의 `paid_amount`를 기준으로 삼는다. 정가(`unit_price`)를
   금액 계산의 기준으로 쓰지 않는다.

## 인터페이스

```python
def allocate_discount(order: Order) -> None:
    """order.discount_total을 품목별 paid_amount로 배분한다."""

def refundable_amount(order: Order, product_id: str) -> int:
    """해당 품목의 환불 가능액(= paid_amount)을 돌려준다."""
```

## 이 계약이 존재하는 이유

쿠폰(A)과 환불(B)이 각자 다른 금액 기준을 가정해 결합 시
과다 환불이 발생했다(사고 기록: 2026-06-30). 금액의 기준을
하나로 고정하는 것이 이 계약의 목적이다.

## 변경 절차

이 계약의 수정은 결제 도메인 오너의 승인과
`tests/test_pricing_contract.py` 갱신을 함께 요구한다.
