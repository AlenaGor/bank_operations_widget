"""
Модуль для работы с виджетами.
"""

from src.masks import mask_account_card


def get_date(date_string: str) -> str:
    """
    Преобразует дату из ISO формата в формат ДД.ММ.ГГГГ.

    Args:
        date_string: Строка с датой в ISO формате

    Returns:
        str: Дата в формате ДД.ММ.ГГГГ
    """
    if not date_string:
        return ''
    try:
        date_part = date_string.split('T')[0]
        year, month, day = date_part.split('-')
        return f"{day}.{month}.{year}"
    except (ValueError, AttributeError):
        return date_string