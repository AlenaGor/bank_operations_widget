"""
Модуль для обработки данных банковских операций.
"""

from typing import List, Dict


def filter_by_state(
    transactions: List[Dict[str, str]],
    state: str = 'EXECUTED'
) -> List[Dict[str, str]]:
    """
    Фильтрует список транзакций по статусу.

    Аргументы:
        transactions: Список словарей с данными транзакций.
        state: Статус для фильтрации (по умолчанию 'EXECUTED').

    Возвращает:
        Новый список транзакций с указанным статусом.
    """
    return [
        item for item in transactions
        if item.get('state') == state
    ]


def sort_by_date(
    transactions: List[Dict[str, str]],
    descending: bool = True
) -> List[Dict[str, str]]:
    """
    Сортирует транзакции по дате.

    Аргументы:
        transactions: Список словарей с данными транзакций.
        descending: True - по убыванию (сначала новые),
                    False - по возрастанию.

    Возвращает:
        Новый список, отсортированный по дате.
    """
    return sorted(
        transactions,
        key=lambda x: x.get('date', ''),
        reverse=descending
    )
