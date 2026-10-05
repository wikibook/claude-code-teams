"""주문 생성."""
from .models import Order, OrderItem


def create_order(order_id: str, items: list[tuple[str, str, int, int]]) -> Order:
    """주문을 생성한다.

    items: (product_id, name, unit_price, quantity) 튜플의 목록
    """
    order = Order(order_id=order_id)
    for product_id, name, unit_price, quantity in items:
        item = OrderItem(product_id, name, unit_price, quantity)
        item.paid_amount = item.list_amount   # 할인 전에는 정가가 지불액
        order.items.append(item)
    return order
