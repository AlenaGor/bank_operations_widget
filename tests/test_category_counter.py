"""
Тесты для модуля category_counter.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.category_counter import count_categories


def test_count_categories():
    """Тест подсчета категорий."""
    transactions = [
        {'description': 'Перевод на карту'},
        {'description': 'Оплата покупки в магазине'},
        {'description': 'Перевод по счету'},
        {'description': 'Оплата коммунальных услуг'}
    ]
    categories = ['Перевод', 'Оплата']
    result = count_categories(transactions, categories)
    assert result == {'Перевод': 2, 'Оплата': 2}


def test_count_categories_empty_transactions():
    """Тест подсчета категорий - пустой список транзакций."""
    result = count_categories([], ['Перевод', 'Оплата'])
    assert result == {'Перевод': 0, 'Оплата': 0}


def test_count_categories_no_match():
    """Тест подсчета категорий - нет совпадений."""
    transactions = [
        {'description': 'Пополнение счета'}
    ]
    categories = ['Перевод', 'Оплата']
    result = count_categories(transactions, categories)
    assert result == {'Перевод': 0, 'Оплата': 0}