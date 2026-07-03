import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("input_str, expected", [
    ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
    ("Счет 1234567890", "Счет **7890"),
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected