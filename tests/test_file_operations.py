"""
Тесты для модуля file_operations.
"""

import pytest
from unittest.mock import Mock, patch
import pandas as pd
from src.file_operations import read_csv_transactions, read_excel_transactions


# Тесты для CSV
@patch('src.file_operations.pd.read_csv')
@patch('src.file_operations.Path')
def test_read_csv_success(mock_path, mock_read_csv):
    """Тест успешного чтения CSV-файла."""
    mock_path_instance = Mock()
    mock_path_instance.exists.return_value = True
    mock_path_instance.stat.return_value.st_size = 100
    mock_path.return_value = mock_path_instance

    # Создаем тестовые данные
    test_data = pd.DataFrame({
        'id': [1, 2, 3],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'amount': [100.50, 50.25, 200.00],
        'category': ['Food', 'Transport', 'Entertainment'],
        'description': ['Grocery shopping', 'Bus ticket', 'Cinema']
    })
    mock_read_csv.return_value = test_data

    result = read_csv_transactions('test.csv')

    assert len(result) == 3
    assert result[0]['id'] == 1
    assert result[0]['amount'] == 100.50
    mock_read_csv.assert_called_once_with('test.csv')


@patch('src.file_operations.Path')
def test_read_csv_file_not_found(mock_path):
    """Тест обработки отсутствующего файла."""
    mock_path_instance = Mock()
    mock_path_instance.exists.return_value = False
    mock_path.return_value = mock_path_instance

    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        read_csv_transactions('nonexistent.csv')


@patch('src.file_operations.Path')
def test_read_csv_empty_file(mock_path):
    """Тест обработки пустого файла."""
    mock_path_instance = Mock()
    mock_path_instance.exists.return_value = True
    mock_path_instance.stat.return_value.st_size = 0
    mock_path.return_value = mock_path_instance

    with pytest.raises(ValueError, match="Файл пустой"):
        read_csv_transactions('empty.csv')


@patch('src.file_operations.pd.read_csv')
@patch('src.file_operations.Path')
def test_read_csv_empty_dataframe(mock_path, mock_read_csv):
    """Тест обработки пустого DataFrame."""
    mock_path_instance = Mock()
    mock_path_instance.exists.return_value = True
    mock_path_instance.stat.return_value.st_size = 100
    mock_path.return_value = mock_path_instance

    empty_df = pd.DataFrame()
    mock_read_csv.return_value = empty_df

    result = read_csv_transactions('empty_data.csv')
    assert result == []


# Тесты для Excel
@patch('src.file_operations.pd.read_excel')
@patch('src.file_operations.Path')
def test_read_excel_success(mock_path, mock_read_excel):
    """Тест успешного чтения Excel-файла."""
    mock_path_instance = Mock()
    mock_path_instance.exists.return_value = True
    mock_path_instance.stat.return_value.st_size = 100
    mock_path_instance.suffix = '.xlsx'
    mock_path.return_value = mock_path_instance

    test_data = pd.DataFrame({
        'id': [1, 2, 3],
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'amount': [100.50, 50.25, 200.00],
        'category': ['Food', 'Transport', 'Entertainment'],
        'description': ['Grocery shopping', 'Bus ticket', 'Cinema']
    })
    mock_read_excel.return_value = test_data

    result = read_excel_transactions('test.xlsx')

    assert len(result) == 3
    assert result[0]['id'] == 1
    mock_read_excel.assert_called_once_with('test.xlsx')


@patch('src.file_operations.Path')
def test_read_excel_file_not_found(mock_path):
    """Тест обработки отсутствующего Excel-файла."""
    mock_path_instance = Mock()
    mock_path_instance.exists.return_value = False
    mock_path.return_value = mock_path_instance

    with pytest.raises(FileNotFoundError, match="Файл не найден"):
        read_excel_transactions('nonexistent.xlsx')


@patch('src.file_operations.Path')
def test_read_excel_empty_file(mock_path):
    """Тест обработки пустого Excel-файла."""
    mock_path_instance = Mock()
    mock_path_instance.exists.return_value = True
    mock_path_instance.stat.return_value.st_size = 0
    mock_path.return_value = mock_path_instance

    with pytest.raises(ValueError, match="Файл пустой"):
        read_excel_transactions('empty.xlsx')


@patch('src.file_operations.Path')
def test_read_excel_invalid_extension(mock_path):
    """Тест обработки неверного расширения файла."""
    mock_path_instance = Mock()
    mock_path_instance.exists.return_value = True
    mock_path_instance.stat.return_value.st_size = 100
    mock_path_instance.suffix = '.txt'
    mock_path.return_value = mock_path_instance

    with pytest.raises(ValueError, match="Неверный формат файла"):
        read_excel_transactions('test.txt')


@patch('src.file_operations.pd.read_excel')
@patch('src.file_operations.Path')
def test_read_excel_empty_dataframe(mock_path, mock_read_excel):
    """Тест обработки пустого DataFrame в Excel."""
    mock_path_instance = Mock()
    mock_path_instance.exists.return_value = True
    mock_path_instance.stat.return_value.st_size = 100
    mock_path_instance.suffix = '.xlsx'
    mock_path.return_value = mock_path_instance

    empty_df = pd.DataFrame()
    mock_read_excel.return_value = empty_df

    result = read_excel_transactions('empty.xlsx')
    assert result == []
