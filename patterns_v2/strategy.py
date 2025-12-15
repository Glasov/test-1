class PaymentStrategy:
    def pay(self, amount):
        pass
    
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Payment {amount} rubles by credit card"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Payment {amount} rubles through PayPal"
    
class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Payment {amount} rubles through bank tranfer"
    
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.items = []
        self.payment_strategy = payment_strategy
    def add_item(self, item):
        self.items.append(item)
    def get_total(self):
        return sum(self.items)
    def checkout(self):
        total = self.get_total()
        return self.payment_strategy.pay(total)
    
cart = ShoppingCart(CreditCardPayment())
cart.add_item(1000)
cart.add_item(2000)
print(cart.checkout())

cart.payment_strategy = PayPalPayment()
print(cart.checkout())
