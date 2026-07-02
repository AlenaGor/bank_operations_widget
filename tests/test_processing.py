"""
Тесты для модуля processing
"""
import pytest
from typing import Any
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations_list() -> list[dict[str, Any]]:
    """Фикстура со списком операций"""
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2020-01-01T12:00:00.000000'},
        {'id': 4, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 5, 'state': 'PENDING', 'date': '2021-05-15T10:30:00.000000'},
    ]


# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_count", [
    ('EXECUTED', 2),
    ('CANCELED', 2),
    ('PENDING', 1),
    ('NON_EXISTENT', 0),
])
def test_filter_by_state(operations_list: list[dict[str, Any]], state: str, expected_count: int) -> None:
    """Тест фильтрации по статусу"""
    result = filter_by_state(operations_list, state)
    assert len(result) == expected_count
    assert all(item['state'] == state for item in result)


def test_filter_by_state_default(operations_list: list[dict[str, Any]]) -> None:
    """Тест фильтрации со статусом по умолчанию"""
    result = filter_by_state(operations_list)
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)


def test_filter_by_state_empty_list() -> None:
    """Тест фильтрации пустого списка"""
    assert filter_by_state([]) == []
    assert filter_by_state([], 'EXECUTED') == []


# Тесты для sort_by_date
def test_sort_by_date_descending(operations_list: list[dict[str, Any]]) -> None:
    """Тест сортировки по убыванию"""
    result = sort_by_date(operations_list)
    dates = [item['date'] for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(operations_list: list[dict[str, Any]]) -> None:
    """Тест сортировки по возрастанию"""
    result = sort_by_date(operations_list, is_descending=False)
    dates = [item['date'] for item in result]
    assert dates == sorted(dates)


def test_sort_by_date_empty_list() -> None:
    """Тест сортировки пустого списка"""
    assert sort_by_date([]) == []
    assert sort_by_date([], is_descending=False) == []