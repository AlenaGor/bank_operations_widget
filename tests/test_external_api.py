import pytest
from unittest.mock import patch, Mock
from src.external_api import convert_currency


def test_convert_currency_rub():
    """Тест конвертации рублёвой транзакции"""
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"}
        }
    }
    result = convert_currency(transaction)
    assert result == 100.5


@patch('src.external_api.requests.get')
def test_convert_currency_usd(mock_get):
    """Тест конвертации USD в рубли"""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9000.0}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response
    
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"}
        }
    }
    
    with patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}):
        result = convert_currency(transaction)
        assert result == 9000.0


@patch('src.external_api.requests.get')
def test_convert_currency_api_error(mock_get):
    """Тест при ошибке API"""
    mock_get.side_effect = Exception("API Error")
    
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"}
        }
    }
    
    with patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}):
        result = convert_currency(transaction)
        assert result == 100.0


def test_convert_currency_missing_api_key():
    """Тест при отсутствии API ключа"""
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"}
        }
    }
    
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(ValueError, match="API ключ не найден"):
            convert_currency(transaction)