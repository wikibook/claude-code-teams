"""개발자 A의 쿠폰 구현 (계약 도입 전).

할인을 주문 '총액'에서 한 번에 차감한다.
품목별 지불액(paid_amount)은 건드리지 않는다 — A의 화면(주문서 합계)에서는
그럴 필요가 없었기 때문이다.
"""
from minishop.models import Order, Coupon


def apply_coupon(order: Order, coupon: Coupon) -> None:
    """쿠폰을 주문에 적용한다. 할인액은 총액 기준으로 계산한다."""
    if order.coupon is not None:
        raise ValueError("쿠폰은 주문당 한 번만 적용할 수 있다")
    order.coupon = coupon
    order.discount_total = round(order.list_total * coupon.rate)
