import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-01-02'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2024-01-03'},
    ]

def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)

def test_sort_by_date(sample_data):
    result = sort_by_date(sample_data)
    assert result[0]['date'] == '2024-01-03'
    assert result[-1]['date'] == '2024-01-01'