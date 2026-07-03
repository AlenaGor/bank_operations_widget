import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

def test_get_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number("12345")

@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("1234567890", "**7890"),
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

def test_get_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account("123")