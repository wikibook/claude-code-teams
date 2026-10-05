"""결합 실패 재현 스크립트 (9.1.1).

개발자 A의 쿠폰 구현과 개발자 B의 환불 구현은 각자의 테스트를 통과했다.
두 코드를 합친 뒤, 쿠폰이 적용된 주문에 부분 환불이 들어오면 무슨 일이
생기는지 재현한다.

실행: python examples/before_contract/reproduce_failure.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from minishop.orders import create_order
from minishop.models import Coupon
from coupons_a import apply_coupon
from refunds_b import refund_item

# 고객이 키보드와 마우스를 주문한다
order = create_order("A-1001", [
    ("P-1", "키보드", 6_000, 1),
    ("P-2", "마우스", 4_000, 1),
])
print(f"정가 합계        : {order.list_total:>6,}원")

# 20% 쿠폰을 적용한다 (개발자 A의 코드)
apply_coupon(order, Coupon(code="WELCOME20", rate=0.2))  # A의 코드
print(f"쿠폰 할인        : {order.discount_total:>6,}원")
print(f"실제 지불액      : {order.paid_total:>6,}원")

# 고객이 키보드를 환불한다 (개발자 B의 코드)
refund = refund_item(order, "P-1")                       # B의 코드
print(f"키보드 환불액    : {refund:>6,}원")

# 장부를 맞춰 본다
remaining_value = order.paid_total - refund
print(f"환불 후 남은 금액: {remaining_value:>6,}원  (마우스 1개 값)")

fair_mouse_price = 4_000 - round(4_000 * 0.2)
print(f"마우스의 할인가  : {fair_mouse_price:>6,}원")
loss = fair_mouse_price - remaining_value
print(f"회사 손실        : {loss:>6,}원  ← 결합 오류")
