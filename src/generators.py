"""
Модуль с генераторами для работы с транзакциями
"""
from typing import Dict, Any, Iterator, List, Union


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по валюте.

    Args:
        transactions: Список словарей с транзакциями
        currency: Код валюты для фильтрации (например, 'USD', 'RUB')

    Yields:
        Словари транзакций с указанной валютой
    """
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций.

    Args:
        transactions: Список словарей с транзакциями

    Yields:
        Описания транзакций
    """
    for transaction in transactions:
        yield transaction.get('description', '')


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: Начальное значение (1-9999999999999999)
        stop: Конечное значение (1-9999999999999999)

    Yields:
        Номера карт в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, stop + 1):
        # Форматируем номер с ведущими нулями до 16 цифр
        card_str = f"{number:016d}"
        # Добавляем пробелы после каждых 4 цифр
        formatted = " ".join(card_str[i:i+4] for i in range(0, 16, 4))
        yield formatted