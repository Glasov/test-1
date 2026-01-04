"""
Паттерн Адаптер (Adapter)
Преобразует интерфейс одного класса в интерфейс другого класса.
"""

# Старая система оплаты (которую нужно адаптировать)
class LegacyPaymentSystem:
    def make_payment(self, customer_id: str, amount_in_cents: int) -> str:
        # Старый метод принимает сумму в центах
        amount_in_rubles = amount_in_cents / 100
        return f"Платеж {amount_in_rubles} руб. от клиента {customer_id} выполнен через Legacy систему"

# Новый интерфейс оплаты (к которому нужно адаптироваться)
class ModernPaymentSystem:
    def process_payment(self, email: str, amount: float) -> str:
        # Новый метод принимает сумму в рублях и email
        return f"Платеж {amount} руб. от {email} выполнен через Modern систему"

# Адаптер
class PaymentAdapter:
    def __init__(self, legacy_system: LegacyPaymentSystem):
        self.legacy_system = legacy_system
    
    def process_payment(self, email: str, amount: float) -> str:
        # Конвертируем email в customer_id (простая логика)
        customer_id = email.split('@')[0]
        
        # Конвертируем рубли в центы
        amount_in_cents = int(amount * 100)
        
        # Используем старую систему
        return self.legacy_system.make_payment(customer_id, amount_in_cents)

# Клиентский код, который работает с ModernPaymentSystem
def process_online_order(payment_system, email: str, amount: float):
    return payment_system.process_payment(email, amount)
