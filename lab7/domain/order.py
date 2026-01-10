from dataclasses import dataclass, field
from typing import List
from decimal import Decimal
from .money import Money
from .order_status import OrderStatus

@dataclass
class OrderLine:
    product_id: str
    product_name: str
    quantity: int
    price: Money
    
    def get_total(self) -> Money:
        return self.price * self.quantity

@dataclass
class Order:
    id: str
    customer_id: str
    lines: List[OrderLine] = field(default_factory=list)
    status: OrderStatus = OrderStatus.CREATED
    
    def add_line(self, product_id: str, product_name: str, quantity: int, price: Money):
        if self.status == OrderStatus.PAID:
            raise ValueError("Cannot modify paid order")
        self.lines.append(OrderLine(product_id, product_name, quantity, price))
    
    def get_total(self) -> Money:
        total = Money(Decimal('0'))
        for line in self.lines:
            total = total + line.get_total()
        return total
    
    def pay(self):
        if self.status == OrderStatus.PAID:
            raise ValueError("Order is already paid")
        if not self.lines:
            raise ValueError("Cannot pay empty order")
        self.status = OrderStatus.PAID
    
    @property
    def is_paid(self) -> bool:
        return self.status == OrderStatus.PAID
