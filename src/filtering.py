"""
Модуль для фильтрации транзакций по описанию
с использованием регулярных выражений.
"""

import re
from typing import List, Dict, Any


def filter_by_description(
    transactions: List[Dict[str, Any]],
    search_string: str
) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по наличию строки в описании
с использованием регулярных выражений.

    Args:
        transactions: Список словарей с транзакциями
        search_string: Строка для поиска

    Returns:
        List[Dict[str, Any]]: Список транзакций, содержащих строку в описании
    """
    if not transactions or not search_string:
        return transactions if transactions else []

    try:
        pattern = re.compile(re.escape(search_string), re.IGNORECASE)
        result = []

        for transaction in transactions:
            description = str(transaction.get('description', ''))
            if pattern.search(description):
                result.append(transaction)

        return result
    except re.error:
        # Если регулярное выражение невалидно, ищем как обычную строку
        search_lower = search_string.lower()
        return [
            t for t in transactions
            if search_lower in str(t.get('description', '')).lower()
        ]
