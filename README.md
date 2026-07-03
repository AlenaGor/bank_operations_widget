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
## Модуль decorators

Модуль содержит декораторы для логирования работы функций.

### `@log(filename=None)`

Декоратор для логирования выполнения функций.

**Параметры:**
- `filename` (опционально): имя файла для записи логов. Если не указан — логи выводятся в консоль.

**Пример использования:**

```python
from src.decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
# В файл mylog.txt будет записано: my_function ok

@log()
def my_function_with_error(x, y):
    return x / y

my_function_with_error(1, 0)
# В консоль будет выведено: my_function_with_error error: ZeroDivisionError. Inputs: (1, 0)
```