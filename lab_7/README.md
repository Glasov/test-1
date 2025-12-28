# Архитектура, слои и DDD-lite
Реализация системы оплаты заказа с разделением по слоям и доменной моделью.
## Структура проекта
```
├── domain/
│ ├── __init__.py
│ ├── money.py 
│ ├── order.py
│ ├── order_line.py
│ └── order_status.py
├── application/
│ ├── __init__.py
│ ├── pay_order_use_case.py
│ └── interfaces.py
├── infrastructure/
│ ├── __init__.py
│ ├── in_memory_order_repository.py
│ └── fake_payment_gateway.py
└── tests/
├── __init__.py
└── test_pay_order.py
```
## Domain
- `Order` — агрегат с бизнес-инвариантами:
  - нельзя оплатить пустой заказ;
  - нельзя оплатить заказ повторно;
  - после оплаты нельзя менять строки заказа.
- `OrderLine` — часть заказа.
- `Money` — value object для работы с деньгами.
- `OrderStatus` — статус заказа (`PENDING`, `PAID`).
## Application
Use-case `PayOrderUseCase`:
  - Загружает заказ через `OrderRepository`.
  - Выполняет оплату через доменную модель.
  - Вызывает платёж через `PaymentGateway`.
  - Сохраняет заказ.
  - Возвращает результат оплаты.
Интерфейсы `OrderRepository` и `PaymentGateway` позволяют use-case работать независимо от конкретной реализации.
## Infrastructure
- `InMemoryOrderRepository` — хранение заказов в памяти.
- `FakePaymentGateway` — имитация оплаты.
## Tests
Unit-тесты проверяют:
  - успешную оплату заказа;
  - ошибку при оплате пустого заказа;
  - ошибку при повторной оплате;
  - невозможность изменения заказа после оплаты;
  - корректный расчёт итоговой суммы.
