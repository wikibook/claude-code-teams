# refunds.py — 개발자 B
"""부분 환불 (계약 적용 후 버전, 개발자 B 담당).

환불액은 품목의 paid_amount를 기준으로 한다.
금액의 기준은 계약(specs/pricing-contract.md)이 정한다.
"""
from .models import Order
from .pricing import refundable_amount


def refund_item(order: Order, product_id: str) -> int:
    """품목 하나를 환불 처리하고 환불액(원)을 돌려준다."""
    amount = refundable_amount(order, product_id)   # 계약: 지불액 기준
    for item in order.items:
        if item.product_id == product_id:
            item.refunded = True
            break
    return amount
