"""개발자 B의 테스트: 부분 환불."""
from minishop.orders import create_order
from minishop.models import Coupon
from minishop.coupons import apply_coupon
from minishop.refunds import refund_item


def test_할인_없는_주문은_정가로_환불된다():
    order = create_order("T-2", [("P-1", "키보드", 6_000, 1)])
    assert refund_item(order, "P-1") == 6_000


def test_쿠폰_주문은_지불액_기준으로_환불된다():
    order = create_order("T-3", [
        ("P-1", "키보드", 6_000, 1),
        ("P-2", "마우스", 4_000, 1),
    ])
    apply_coupon(order, Coupon("WELCOME20", 0.2))
    assert refund_item(order, "P-1") == 4_800   # 정가 6,000이 아니다


def test_같은_품목은_두_번_환불되지_않는다():
    order = create_order("T-4", [("P-1", "키보드", 6_000, 1)])
    refund_item(order, "P-1")
    try:
        refund_item(order, "P-1")
        assert False, "중복 환불은 실패해야 한다"
    except ValueError:
        pass
