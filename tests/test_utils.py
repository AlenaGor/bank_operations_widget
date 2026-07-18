import pytest
import json
import os
from src.utils import get_transactions_from_json


def test_get_transactions_from_json_success(tmp_path):
    """Тест успешного чтения JSON-файла"""
    # Создаём временный JSON-файл
    test_data = [{"id": 1, "amount": 100}]
    file_path = tmp_path / "test.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f)

    result = get_transactions_from_json(str(file_path))
    assert result == test_data


def test_get_transactions_from_json_empty(tmp_path):
    """Тест с пустым файлом"""
    file_path = tmp_path / "empty.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("")

    result = get_transactions_from_json(str(file_path))
    assert result == []


def test_get_transactions_from_json_not_list(tmp_path):
    """Тест с JSON, который не является списком"""
    file_path = tmp_path / "not_list.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({"key": "value"}, f)

    result = get_transactions_from_json(str(file_path))
    assert result == []


def test_get_transactions_from_json_not_found():
    """Тест с несуществующим файлом"""
    result = get_transactions_from_json("nonexistent.json")
    assert result == []