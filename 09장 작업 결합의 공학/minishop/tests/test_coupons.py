"""개발자 A의 테스트: 쿠폰 적용."""
from minishop.orders import create_order
from minishop.models import Coupon
from minishop.coupons import apply_coupon


def make_order():
    return create_order("T-1", [
        ("P-1", "키보드", 6_000, 1),
        ("P-2", "마우스", 4_000, 1),
    ])


def test_쿠폰_적용시_총액이_할인된다():
    order = make_order()
    apply_coupon(order, Coupon("WELCOME20", 0.2))
    assert order.discount_total == 2_000
    assert order.paid_total == 8_000


def test_쿠폰은_한_번만_적용된다():
    order = make_order()
    apply_coupon(order, Coupon("WELCOME20", 0.2))
    try:
        apply_coupon(order, Coupon("EXTRA10", 0.1))
        assert False, "두 번째 적용은 실패해야 한다"
    except ValueError:
        pass


def test_할인이_품목에_배분된다():
    order = make_order()
    apply_coupon(order, Coupon("WELCOME20", 0.2))
    keyboard, mouse = order.items
    assert keyboard.paid_amount == 4_800
    assert mouse.paid_amount == 3_200
