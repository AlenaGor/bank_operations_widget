# Виджет банковских операций

## Описание
Проект для обработки данных банковских операций.

## Функции
- `filter_by_state()` - фильтрация по статусу
- `sort_by_date()` - сортировка по дате

## Модуль utils

### `get_transactions_from_json(file_path)`

Читает JSON-файл с транзакциями и возвращает список словарей.

```python
from src.utils import get_transactions_from_json

transactions = get_transactions_from_json("data/operations.json")

from src.external_api import convert_currency

transaction = {
    "operationAmount": {
        "amount": "100.00",
        "currency": {"code": "USD"}
    }
}
result = convert_currency(transaction)  # возвращает сумму в рублях

### Настройка
Создайте файл .env в корне проекта:
EXCHANGE_RATES_API_KEY=ваш_ключ_от_apilayer

---

## Установи зависимости

```bash
pip install requests python-dotenv