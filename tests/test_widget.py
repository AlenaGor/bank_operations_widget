"""
Тесты для модуля widget
"""
import pytest
from src.widget import mask_account_card, get_date


# Тесты для mask_account_card
@pytest.mark.parametrize("input_str, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(input_str, expected):
    """Тест маскировки карты или счета"""
    assert mask_account_card(input_str) == expected


def test_mask_account_card_invalid_input():
    """Тест на некорректный ввод"""
    with pytest.raises(ValueError, match="Строка должна содержать тип и номер карты/счета"):
        mask_account_card("Только_тип")


def test_mask_account_card_empty_input():
    """Тест на пустую строку"""
    with pytest.raises(ValueError, match="Строка должна содержать тип и номер карты/счета"):
        mask_account_card("")


# Тесты для get_date
@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-25T10:15:30.123456", "25.12.2023"),
    ("2024-01-01T00:00:00", "01.01.2024"),
])
def test_get_date(input_date, expected):
    """Тест преобразования даты"""
    assert get_date(input_date) == expected


def test_get_date_invalid_format():
    """Тест на некорректный формат даты"""
    with pytest.raises(ValueError):
        get_date("2024/03/11")
        