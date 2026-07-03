# Виджет банковских операций

## Описание
Проект для обработки данных банковских операций.

## Функции
- `filter_by_state()` - фильтрация по статусу
- `sort_by_date()` - сортировка по дате

## Модуль generators

Модуль содержит генераторы для работы с транзакциями.

### `filter_by_currency(transactions, currency)`

Фильтрует транзакции по валюте.

```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
```

---

### `transaction_descriptions(transactions)`

Генерирует описания транзакций.

```python
from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)
```

---

### `card_number_generator(start, stop)`

Генерирует номера банковских карт.

```python
from src.generators import card_number_generator

for card in card_number_generator(1, 5):
    print(card)
# 0000 0000 0000 0001
# 0000 0000 0000 0002
```