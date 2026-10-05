"""주문 생성 테스트."""
from minishop.orders import create_order


def test_주문_생성():
    order = create_order("T-0", [
        ("P-1", "키보드", 6_000, 1),
        ("P-2", "마우스", 4_000, 2),
    ])
    assert order.list_total == 14_000
    assert order.paid_total == 14_000   # 할인 전
    assert order.items[1].paid_amount == 8_000
