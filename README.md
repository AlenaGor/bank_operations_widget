# Виджет банковских операций

## Описание
Проект для обработки данных банковских операций. Содержит функции для фильтрации, сортировки, маскировки данных, работу с JSON-файлами, конвертацию валют и логирование.

---

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ВАШ_АККАУНТ/bank_operations_widget.git
cd bank_operations_widget
```

2. Создайте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
.venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

---

## Настройка

Создайте файл `.env` в корне проекта на основе `.env.example`:

```bash
cp .env.example .env
```

Заполните файл `.env` своими данными:
```
EXCHANGE_RATES_API_KEY=ваш_ключ_от_apilayer
```

Получить API ключ можно на сайте [apilayer.com](https://apilayer.com/exchangerates_data-api).

---

## Модули и функции

### Модуль `masks.py`

#### `get_mask_card_number(card_number)`
Маскирует номер банковской карты (16 цифр).

```python
from src.masks import get_mask_card_number

masked = get_mask_card_number("7000792289606361")
print(masked)  # "7000 79** **** 6361"
```

#### `get_mask_account(account_number)`
Маскирует номер банковского счета.

```python
from src.masks import get_mask_account

masked = get_mask_account("73654108430135874305")
print(masked)  # "**4305"
```

---

### Модуль `widget.py`

#### `mask_account_card(card_or_account_info)`
Принимает строку с типом и номером карты/счета, возвращает замаскированную версию.

```python
from src.widget import mask_account_card

result = mask_account_card("Visa Platinum 7000792289606361")
print(result)  # "Visa Platinum 7000 79** **** 6361"

result = mask_account_card("Счет 73654108430135874305")
print(result)  # "Счет **4305"
```

#### `get_date(date_string)`
Преобразует дату из ISO формата в формат ДД.ММ.ГГГГ.

```python
from src.widget import get_date

date = get_date("2024-03-11T02:26:18.671407")
print(date)  # "11.03.2024"
```

---

### Модуль `processing.py`

#### `filter_by_state(operations, state='EXECUTED')`
Фильтрует список операций по статусу.

```python
from src.processing import filter_by_state

transactions = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'CANCELED'},
    {'id': 3, 'state': 'EXECUTED'}
]

executed = filter_by_state(transactions)
print(executed)  # только операции с state='EXECUTED'
```

#### `sort_by_date(operations, is_descending=True)`
Сортирует список операций по дате.

```python
from src.processing import sort_by_date

sorted_ops = sort_by_date(transactions, is_descending=False)
```

---

### Модуль `generators.py`

#### `filter_by_currency(transactions, currency)`
Фильтрует транзакции по валюте. Возвращает итератор.

```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
```

#### `transaction_descriptions(transactions)`
Генерирует описания транзакций.

```python
from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)
```

#### `card_number_generator(start, stop)`
Генерирует номера банковских карт.

```python
from src.generators import card_number_generator

for card in card_number_generator(1, 5):
    print(card)
```

---

### Модуль `decorators.py`

#### `@log(filename=None)`
Декоратор для логирования выполнения функций.

```python
from src.decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)  # запись в файл mylog.txt
```

---

### Модуль `utils.py`

#### `get_transactions_from_json(file_path)`
Читает JSON-файл с транзакциями и возвращает список словарей.

```python
from src.utils import get_transactions_from_json

transactions = get_transactions_from_json("data/operations.json")
```

---

### Модуль `file_operations.py` (НОВЫЙ)

Поддерживает чтение финансовых операций из CSV и Excel файлов.

#### `read_csv_transactions(file_path)`
Читает финансовые операции из CSV-файла.

```python
from src.file_operations import read_csv_transactions

transactions = read_csv_transactions("data/transactions.csv")
```

#### `read_excel_transactions(file_path)`
Читает финансовые операции из Excel-файла (XLSX).

```python
from src.file_operations import read_excel_transactions

transactions = read_excel_transactions("data/transactions_excel.xlsx")
```

---

### Модуль `external_api.py`

#### `convert_currency(transaction)`
Конвертирует сумму транзакции в рубли.

```python
from src.external_api import convert_currency

transaction = {
    "operationAmount": {
        "amount": "100.00",
        "currency": {"code": "USD"}
    }
}

result = convert_currency(transaction)  # сумма в рублях
```

---

## Логирование

Проект использует библиотеку `logging` для записи логов.

### Логи

Логи записываются в папку `logs/`:

| Модуль | Файл лога |
|--------|-----------|
| `utils` | `logs/utils.log` |
| `masks` | `logs/masks.log` |
| `processing` | `logs/processing.log` |
| `file_operations` | `logs/file_operations.log` |

### Формат логов

```
2024-07-18 12:30:45,123 - src.utils - INFO - Попытка открыть файл: data/operations.json
2024-07-18 12:30:45,234 - src.masks - DEBUG - Успешно замаскирован номер карты
```

### Настройка

Логи перезаписываются при каждом запуске приложения.

---

## Тестирование

### Запуск тестов:

```bash
# Запустить все тесты
pytest tests/

# Запустить тесты с подробным выводом
pytest tests/ -v

# Запустить тесты для file_operations
pytest tests/test_file_operations.py -v
```

### Проверка покрытия:

```bash
# Проверить покрытие всех модулей
pytest --cov=src --cov-report=term

# Проверить покрытие конкретного модуля
pytest --cov=src.file_operations tests/test_file_operations.py

# Создать HTML отчет
pytest --cov=src --cov-report=html
```

### Проверка стиля кода:

```bash
# Проверить весь проект
flake8 src/ tests/

# Проверить только новые модули
flake8 src/file_operations.py tests/test_file_operations.py
```

### Статус тестирования:
- ✅ Все тесты проходят (9/9 для file_operations)
- ✅ Покрытие file_operations - 88%
- ✅ Flake8 для нового кода - 0 ошибок

---

## Требования

- Python 3.12+
- requests
- python-dotenv
- pytest
- pytest-cov
- pandas
- openpyxl

---

## Лицензия

MIT