from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str = "USD"
    
    def __post_init__(self):
        if self.amount < Decimal('0'):
            raise ValueError("Amount cannot be negative")
    
    def __add__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Can only add Money to Money")
        if self.currency != other.currency:
            raise ValueError("Currencies must match")
        return Money(self.amount + other.amount, self.currency)
    
    def __mul__(self, quantity):
        return Money(self.amount * Decimal(str(quantity)), self.currency)
    
    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"
