# Виджет банковских операций

## Описание
Проект для обработки и фильтрации данных банковских операций.

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/AlenaGor/bank_operations_widget.git
cd bank_operations_widget
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
.venv\Scripts\activate     # для Windows
# или
source .venv/bin/activate  # для Linux/Mac
```

3. Установите зависимости (если есть):
```bash
pip install -r requirements.txt
```

## Зависимости
Проект использует только стандартную библиотеку Python, дополнительные зависимости не требуются.

## Использование

```python
from src.processing import filter_by_state, sort_by_date

# Данные по операциям
operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T10:00:00'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02T10:00:00'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03T10:00:00'}
]

# Фильтрация по статусу (по умолчанию 'EXECUTED')
executed_operations = filter_by_state(operations)
print(executed_operations)

# Фильтрация с указанием статуса
canceled_operations = filter_by_state(operations, 'CANCELED')
print(canceled_operations)

# Сортировка по дате (по умолчанию по убыванию — сначала новые)
sorted_operations = sort_by_date(operations)
print(sorted_operations)
```

## Функции

### `filter_by_state(transactions, state='EXECUTED')`
Фильтрует список транзакций по статусу.

**Параметры:**
- `transactions` (List[Dict[str, str]]) — список словарей с данными транзакций
- `state` (str) — статус для фильтрации (по умолчанию `'EXECUTED'`)

**Возвращает:** Новый список транзакций с указанным статусом.

---

### `sort_by_date(transactions, descending=True)`
Сортирует транзакции по дате.

**Параметры:**
- `transactions` (List[Dict[str, str]]) — список словарей с данными транзакций
- `descending` (bool) — `True` — по убыванию (сначала новые), `False` — по возрастанию

**Возвращает:** Новый список, отсортированный по дате.

## Требования
- Python 3.8+
- Зависимости отсутствуют

## Лицензия
MIT
