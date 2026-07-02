"""
Тесты для модуля masks
"""
import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
    ("1111222233334444", "1111 22** **** 4444"),
])
def test_get_mask_card_number(card_number: str, expected: str):
    """Тест маскировки номера карты"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_length():
    """Тест на некорректную длину номера карты"""
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number("12345")


def test_get_mask_card_number_non_digit():
    """Тест на нецифровые символы в номере карты"""
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр"):
        get_mask_card_number("1234abcd12345678")


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("1234567890", "**7890"),
    ("11111111111111111111", "**1111"),
])
def test_get_mask_account(account_number: str, expected: str):
    """Тест маскировки номера счета"""
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid_length():
    """Тест на слишком короткий номер счета"""
    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 4 цифры"):
        get_mask_account("123")


def test_get_mask_account_non_digit():
    """Тест на нецифровые символы в номере счета"""
    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 4 цифры"):
        get_mask_account("abcd")
        