"""
Тесты для модуля generators
"""
import pytest
from typing import Any, Dict, List
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми транзакциями"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод с карты на карту",
        },
    ]


# Тесты для filter_by_currency
@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 3),
    ("RUB", 1),
    ("EUR", 0),
])
def test_filter_by_currency(sample_transactions, currency, expected_count):
    """Тест фильтрации по валюте"""
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(t['operationAmount']['currency']['code'] == currency for t in result)


def test_filter_by_currency_empty():
    """Тест с пустым списком"""
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_by_currency_no_matches(sample_transactions):
    """Тест когда нет транзакций с нужной валютой"""
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_filter_by_currency_iterator(sample_transactions):
    """Тест что функция возвращает итератор"""
    result = filter_by_currency(sample_transactions, "USD")
    assert hasattr(result, '__iter__')
    assert hasattr(result, '__next__')


# Тесты для transaction_descriptions
def test_transaction_descriptions(sample_transactions):
    """Тест генерации описаний"""
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == expected


def test_transaction_descriptions_empty():
    """Тест с пустым списком"""
    result = list(transaction_descriptions([]))
    assert result == []


def test_transaction_descriptions_missing_key():
    """Тест когда у транзакции нет описания"""
    transactions = [{"id": 1}, {"id": 2, "description": "Тест"}]
    result = list(transaction_descriptions(transactions))
    assert result == ["", "Тест"]


# Тесты для card_number_generator
@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (5, 5, ["0000 0000 0000 0005"]),
    (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
])
def test_card_number_generator(start, stop, expected):
    """Тест генерации номеров карт"""
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_format():
    """Тест форматирования номеров карт"""
    for card in card_number_generator(1, 1):
        assert len(card) == 19  # 16 цифр + 3 пробела
        parts = card.split()
        assert len(parts) == 4
        assert all(len(part) == 4 for part in parts)
        assert all(part.isdigit() for part in parts)


def test_card_number_generator_range():
    """Тест что генератор выдаёт правильное количество номеров"""
    result = list(card_number_generator(1, 10))
    assert len(result) == 10

    result2 = list(card_number_generator(100, 120))
    assert len(result2) == 21