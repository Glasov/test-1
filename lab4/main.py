"""
Главный файл для тестирования всех паттернов Лабы 4
"""

print("=" * 60)
print("ЛАБОРАТОРНАЯ РАБОТА №4")
print("ПОВЕДЕНЧЕСКИЕ И СТРУКТУРНЫЕ ПАТТЕРНЫ")
print("=" * 60)

# =================== ПОВЕДЕНЧЕСКИЕ ПАТТЕРНЫ ===================

print("\n" + "=" * 60)
print("1. ПОВЕДЕНЧЕСКИЕ ПАТТЕРНЫ")
print("=" * 60)

# 1.1 Стратегия
print("\n--- 1.1 СТРАТЕГИЯ (Strategy) ---")
from behavioral.strategy.payment_strategy import ShoppingCart, CreditCardPayment, PayPalPayment, BitcoinPayment

cart = ShoppingCart()
cart.add_item("Книга", 500)
cart.add_item("Наушники", 3000)

# Оплата кредитной картой
cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456", "123"))
print(cart.checkout())

# Оплата через PayPal
cart.set_payment_strategy(PayPalPayment("user@example.com"))
print(cart.checkout())

# Оплата биткоинами
cart.set_payment_strategy(BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
print(cart.checkout())

# 1.2 Цепочка обязанностей
print("\n--- 1.2 ЦЕПОЧКА ОБЯЗАННОСТЕЙ (Chain of Responsibility) ---")
from behavioral.chain_of_responsibility.logger_chain import Application

app = Application()
print("Логирование событий:")
app.process_event("Приложение запущено", "INFO")
app.process_event("Недостаточно памяти", "WARNING")
app.process_event("Критическая ошибка!", "ERROR")
app.process_event("Отладочная информация", "DEBUG")

# 1.3 Итератор
print("\n--- 1.3 ИТЕРАТОР (Iterator) ---")
from behavioral.iterator.book_collection import BookCollection, Book

library = BookCollection()
library.add_book(Book("Война и мир", "Лев Толстой"))
library.add_book(Book("Преступление и наказание", "Федор Достоевский"))
library.add_book(Book("Мастер и Маргарита", "Михаил Булгаков"))

print("Книги в коллекции (прямой порядок):")
for book in library:
    print(f"  - {book}")

print("\nКниги в коллекции (обратный порядок):")
reverse_iter = library.get_reverse_iterator()
for book in reverse_iter:
    print(f"  - {book}")

# =================== СТРУКТУРНЫЕ ПАТТЕРНЫ ===================

print("\n" + "=" * 60)
print("2. СТРУКТУРНЫЕ ПАТТЕРНЫ")
print("=" * 60)

# 2.1 Прокси
print("\n--- 2.1 ПРОКСИ (Proxy) ---")
from structural.proxy.youtube_proxy import YouTubeProxy

print("Использование прокси для видео:")
video_proxy = YouTubeProxy("Изучаем паттерны проектирования")
print(video_proxy.get_info())  # Быстро - без загрузки видео
print(video_proxy.play())      # Первый раз - загружает видео
print(video_proxy.play())      # Второй раз - использует кэш

# 2.2 Мост
print("\n--- 2.2 МОСТ (Bridge) ---")
from structural.bridge.device_bridge import TV, Radio, RemoteControl, AdvancedRemoteControl

print("\nУправление TV:")
tv = TV()
tv_remote = RemoteControl(tv)
tv_remote.toggle_power()
tv_remote.volume_up()
tv_remote.volume_up()
tv_remote.volume_down()
tv_remote.toggle_power()

print("\nУправление Radio (расширенный пульт):")
radio = Radio()
radio_remote = AdvancedRemoteControl(radio)
radio_remote.toggle_power()
radio_remote.volume_up()
radio_remote.mute()
radio_remote.toggle_power()

# 2.3 Адаптер
print("\n--- 2.3 АДАПТЕР (Adapter) ---")
from structural.adapter.payment_adapter import LegacyPaymentSystem, ModernPaymentSystem, PaymentAdapter, process_online_order

print("\nРабота с Modern системой:")
modern_system = ModernPaymentSystem()
print(process_online_order(modern_system, "ivan@mail.com", 1500.50))

print("\nРабота с Legacy системой через адаптер:")
legacy_system = LegacyPaymentSystem()
adapter = PaymentAdapter(legacy_system)
print(process_online_order(adapter, "petr@gmail.com", 2500.75))

print("\n" + "=" * 60)
print("ВСЕ 6 ПАТТЕРНОВ УСПЕШНО ПРОТЕСТИРОВАНЫ!")
print("=" * 60)

print("\nИтого реализовано:")
print("1. Стратегия (Strategy) - система оплаты")
print("2. Цепочка обязанностей (Chain of Responsibility) - логирование")
print("3. Итератор (Iterator) - коллекция книг")
print("4. Прокси (Proxy) - YouTube видео с кэшированием")
print("5. Мост (Bridge) - пульты управления устройствами")
print("6. Адаптер (Adapter) - платежные системы")
