"""
Виджет банковских операций
"""
from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime


def mask_account_card(card_or_account_info: str) -> str:
    """
    Принимает строку с типом и номером карты/счета и возвращает замаскированную версию
    """
    parts = card_or_account_info.strip().split()
    if len(parts) < 2:
        raise ValueError("Строка должна содержать тип и номер карты/счета")

    card_type = " ".join(parts[:-1])
    number = parts[-1]

    if card_type.lower() == "счет":
        return f"{card_type} {get_mask_account(number)}"
    else:
        return f"{card_type} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из ISO формата в формат ДД.ММ.ГГГГ
    """
    date_part = date_string.split('T')[0]
    date_obj = datetime.strptime(date_part, "%Y-%m-%d")
    return date_obj.strftime("%d.%m.%Y")