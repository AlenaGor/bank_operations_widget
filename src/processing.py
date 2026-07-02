"""
Модуль для обработки данных банковских операций.
"""

from typing import List, Dict


def filter_by_state(transactions: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Фильтрует список транзакций по статусу.

    Аргументы:
        transactions: Список словарей с данными транзакций.
        state: Статус для фильтрации (по умолчанию 'EXECUTED').

    Возвращает:
        Новый список транзакций с указанным статусом.
    """
    return [item for item in transactions if item.get('state') == state]


def sort_by_date(operations: list[dict[str, Any]], is_descending: bool = True) -> list[dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Args:
        operations: Список словарей с данными об операциях
        is_descending: Порядок сортировки (True - убывание, False - возрастание)

    Returns:
        Новый отсортированный список операций
    """
    return sorted(operations, key=lambda x: x.get('date', ''), reverse=is_descending)