"""할인 배분 규칙 — specs/pricing-contract.md의 구현.

주문 수준 할인을 품목 단위로 배분한다. 배분 규칙과 불변식은
계약 문서에 정의되어 있으며, tests/test_pricing_contract.py가 검증한다.
"""
from .models import Order


def allocate_discount(order: Order) -> None:
    """order.discount_total을 품목별 paid_amount로 배분한다."""
    total = order.list_total
    if total == 0 or order.discount_total == 0:
        for item in order.items:
            item.paid_amount = item.list_amount
        return

    # 1차 배분: 정가 비율대로 내림 계산
    discounts = []
    for item in order.items:
        share = order.discount_total * item.list_amount // total
        discounts.append(share)

    # 잔차 배분: 남은 금액을 정가가 큰 품목부터 1원씩
    remainder = order.discount_total - sum(discounts)
    order_by_amount = sorted(range(len(order.items)),
        key=lambda i: order.items[i].list_amount, reverse=True)
    for i in order_by_amount[:remainder]:
        discounts[i] += 1

    for item, discount in zip(order.items, discounts):
        item.paid_amount = item.list_amount - discount


def refundable_amount(order: Order, product_id: str) -> int:
    """해당 품목의 환불 가능액(= paid_amount)을 돌려준다."""
    for item in order.items:
        if item.product_id == product_id and not item.refunded:
            return item.paid_amount
    raise ValueError(f"환불할 품목이 없다: {product_id}")
