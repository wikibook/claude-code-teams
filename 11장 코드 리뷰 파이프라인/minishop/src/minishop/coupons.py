# coupons.py — 개발자 A
"""쿠폰 적용 (계약 적용 후 버전, 개발자 A 담당).

할인 총액을 계산한 뒤, 품목 배분은 pricing.allocate_discount에 맡긴다.
금액의 기준은 계약(specs/pricing-contract.md)이 정한다.
"""
from .models import Order, Coupon
from .pricing import allocate_discount


def apply_coupon(order: Order, coupon: Coupon) -> None:
    """쿠폰을 주문에 적용하고 할인액을 품목에 배분한다."""
    if order.coupon is not None:
        raise ValueError("쿠폰은 주문당 한 번만 적용할 수 있다")
    order.coupon = coupon
    order.discount_total = round(order.list_total * coupon.rate)
    allocate_discount(order)   # 계약: 할인은 품목 단위로 배분한다
