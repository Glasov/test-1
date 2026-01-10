"""
Паттерн Стратегия (Strategy)
Определяет семейство алгоритмов, инкапсулирует каждый из них
и делает их взаимозаменяемыми.
"""

from abc import ABC, abstractmethod

# Интерфейс стратегии
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

# Конкретные стратегии
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount: float) -> str:
        return f"Оплачено {amount} руб. кредитной картой {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> str:
        return f"Оплачено {amount} руб. через PayPal ({self.email})"

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def pay(self, amount: float) -> str:
        return f"Оплачено {amount} руб. биткоинами на адрес {self.wallet_address[:10]}..."

# Контекст
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item: str, price: float):
        self.items.append((item, price))
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy
    
    def checkout(self) -> str:
        if not self.payment_strategy:
            return "Ошибка: не выбран способ оплаты"
        
        total = sum(price for _, price in self.items)
        result = self.payment_strategy.pay(total)
        
        items_str = ", ".join([f"{item} ({price} руб.)" for item, price in self.items])
        return f"Покупка: {items_str}\n{result}"
