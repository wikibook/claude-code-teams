"""계약 테스트: specs/pricing-contract.md의 불변식을 검증한다.

이 테스트가 깨지면 계약 위반이다. 구현을 계약에 맞추거나,
계약 변경 절차(오너 승인)를 거쳐야 한다.
"""
from minishop.orders import create_order
from minishop.models import Coupon
from minishop.coupons import apply_coupon
from minishop.pricing import refundable_amount
from minishop.refunds import refund_item


def make_discounted_order(items, rate=0.2):
    order = create_order("C-1", items)
    apply_coupon(order, Coupon("TEST", rate))
    return order


def test_불변식_품목_지불액의_합은_주문_지불액과_같다():
    # 나누어떨어지지 않는 금액으로 잔차 처리까지 검증한다
    order = make_discounted_order([
        ("P-1", "키보드", 6_990, 1),
        ("P-2", "마우스", 4_990, 1),
        ("P-3", "패드", 1_010, 3),
    ], rate=0.15)
    assert sum(i.paid_amount for i in order.items) == order.paid_total


def test_환불액은_지불액을_기준으로_한다():
    order = make_discounted_order([
        ("P-1", "키보드", 6_000, 1),
        ("P-2", "마우스", 4_000, 1),
    ])
    keyboard = order.items[0]
    assert refundable_amount(order, "P-1") == keyboard.paid_amount


def test_전_품목_환불액의_합은_지불_총액과_같다():
    order = make_discounted_order([
        ("P-1", "키보드", 6_000, 1),
        ("P-2", "마우스", 4_000, 1),
        ("P-3", "패드", 3_500, 2),
    ], rate=0.2)
    expected_total = order.paid_total
    refund_sum = sum(refund_item(order, i.product_id) for i in order.items)
    assert refund_sum == expected_total   # 과다·과소 환불 없음
