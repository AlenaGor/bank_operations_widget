"""
Тесты для модуля filtering.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.filtering import filter_by_description


def test_filter_by_description_found():
    """Тест поиска по описанию - найдено."""
    transactions = [
        {'description': 'Перевод на карту'},
        {'description': 'Оплата покупки'},
        {'description': 'Перевод по счету'}
    ]
    result = filter_by_description(transactions, 'Перевод')
    assert len(result) == 2
    assert all('Перевод' in t['description'] for t in result)


def test_filter_by_description_not_found():
    """Тест поиска по описанию - не найдено."""
    transactions = [
        {'description': 'Перевод на карту'},
        {'description': 'Оплата покупки'}
    ]
    result = filter_by_description(transactions, 'Пополнение')
    assert len(result) == 0


def test_filter_by_description_empty():
    """Тест поиска по описанию - пустой список."""
    result = filter_by_description([], 'Перевод')
    assert result == []


def test_filter_by_description_case_insensitive():
    """Тест поиска по описанию - регистронезависимый."""
    transactions = [
        {'description': 'перевод на карту'},
        {'description': 'ПЕРЕВОД по счету'}
    ]
    result = filter_by_description(transactions, 'перевод')
    assert len(result) == 2