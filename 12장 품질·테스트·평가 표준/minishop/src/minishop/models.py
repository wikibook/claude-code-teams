"""미니숍 데이터 모델. 금액은 원 단위 정수로 다룬다."""
from dataclasses import dataclass, field


@dataclass
class OrderItem:
    """주문 품목."""
    product_id: str
    name: str
    unit_price: int   # 정가(원)
    quantity: int
    paid_amount: int = 0   # 품목의 실제 지불액(원)
    refunded: bool = False

    @property
    def list_amount(self) -> int:
        """정가 기준 금액."""
        return self.unit_price * self.quantity


@dataclass
class Coupon:
    """정률 할인 쿠폰."""
    code: str
    rate: float   # 0.2 = 20% 할인


@dataclass
class Order:
    """주문. 생성 직후에는 할인이 없는 상태다."""
    order_id: str
    items: list[OrderItem] = field(default_factory=list)
    coupon: Coupon | None = None
    discount_total: int = 0   # 주문 전체 할인액(원)

    @property
    def list_total(self) -> int:
        """정가 합계."""
        return sum(item.list_amount for item in self.items)

    @property
    def paid_total(self) -> int:
        """실제 지불 합계."""
        return self.list_total - self.discount_total
