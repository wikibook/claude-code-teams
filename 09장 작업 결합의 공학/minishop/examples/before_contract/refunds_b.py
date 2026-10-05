"""개발자 B의 부분 환불 구현 (계약 도입 전).

품목의 '정가'를 기준으로 환불액을 계산한다.
B가 받은 요구사항과 B가 본 코드(models.py)에는 할인이 품목에
어떻게 배분되는지에 대한 정보가 없었다 — 그래서 B는 정가를 기준으로 삼았다.
"""
from minishop.models import Order


def refund_item(order: Order, product_id: str) -> int:
    """품목 하나를 환불 처리하고 환불액(원)을 돌려준다."""
    for item in order.items:
        if item.product_id == product_id and not item.refunded:
            item.refunded = True
            return item.unit_price * item.quantity   # 정가 기준 환불
    raise ValueError(f"환불할 품목이 없다: {product_id}")
