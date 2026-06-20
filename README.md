# Виджет банковских операций

## Описание
Проект для обработки и фильтрации данных банковских операций.

## Установка

1. Клонируйте репозиторий:
git clone https://github.com/AlenaGor/bank_operations_widget.git
cd bank_operations_widget

## Использование

from src.processing import filter_by_state, sort_by_date

# Данные по операциям
operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T10:00:00'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02T10:00:00'},
]

# Фильтрация
executed = filter_by_state(operations)

# Сортировка
sorted_ops = sort_by_date(operations)

## Функции

- filter_by_state() - фильтрация по статусу
- sort_by_date() - сортировка по дате
- 