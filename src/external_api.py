"""
Модуль для работы с внешними API
"""
import os
import requests
from typing import Dict, Any


def convert_currency(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма транзакции в рублях (float).
        Если транзакция уже в рублях — возвращает сумму как есть.
        Если в USD/EUR — конвертирует через API.
    """
    # Получаем сумму и валюту из транзакции
    operation_amount = transaction.get('operationAmount', {})
    amount_str = operation_amount.get('amount', '0')
    currency_code = operation_amount.get('currency', {}).get('code', 'RUB')

    amount = float(amount_str)

    # Если валюта уже рубли — возвращаем сумму
    if currency_code == 'RUB':
        return amount

    # Если USD или EUR — конвертируем через API
    if currency_code in ('USD', 'EUR'):
        api_key = os.getenv('EXCHANGE_RATES_API_KEY')
        if not api_key:
            raise ValueError("API ключ не найден. Установите EXCHANGE_RATES_API_KEY в .env")

        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {
            'from': currency_code,
            'to': 'RUB',
            'amount': amount
        }
        headers = {'apikey': api_key}

        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data.get('result', amount)
        except Exception:
            # В случае ошибки API возвращаем исходную сумму
            return amount

    # Для других валют возвращаем исходную сумму
    return amount