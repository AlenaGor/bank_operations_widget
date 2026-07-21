"""
Модуль для подсчета количества операций по категориям.
"""

from collections import Counter
from typing import List, Dict, Any


def count_categories(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории.

    Args:
        transactions: Список словарей с транзакциями
        categories: Список категорий для подсчета

    Returns:
        Dict[str, int]: Словарь с количеством операций в каждой категории
    """
    if not transactions:
        return {category: 0 for category in categories}

    category_counter = Counter()

    for transaction in transactions:
        description = str(transaction.get('description', '')).lower()
        for category in categories:
            if category.lower() in description:
                category_counter[category] += 1
                break

    result = {category: category_counter.get(category, 0) for category in categories}

    return result