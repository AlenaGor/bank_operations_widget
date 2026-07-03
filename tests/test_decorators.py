"""
Тесты для модуля decorators
"""
import pytest
import os
from src.decorators import log


# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ (без префикса test_)
@log()
def function_ok(a: int, b: int) -> int:
    """Функция, которая работает без ошибок"""
    return a + b


@log()
def function_error(a: int, b: int) -> float:
    """Функция, которая вызывает ошибку"""
    return a / b


@log(filename="test_log.txt")
def function_file_ok(a: int, b: int) -> int:
    """Функция с записью в файл"""
    return a + b


@log(filename="test_log.txt")
def function_file_error(a: int, b: int) -> float:
    """Функция с ошибкой и записью в файл"""
    return a / b


# ТЕСТЫ
def test_log_console_ok(capsys):
    """Тест вывода в консоль при успешном выполнении"""
    result = function_ok(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert "function_ok ok" in captured.out


def test_log_console_error(capsys):
    """Тест вывода в консоль при ошибке"""
    with pytest.raises(ZeroDivisionError):
        function_error(5, 0)

    captured = capsys.readouterr()
    assert "function_error error: ZeroDivisionError" in captured.out
    assert "Inputs: (5, 0)" in captured.out


def test_log_file_ok():
    """Тест записи в файл при успешном выполнении"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    result = function_file_ok(10, 20)
    assert result == 30

    assert os.path.exists("test_log.txt")

    with open("test_log.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        assert "function_file_ok ok" in content

    os.remove("test_log.txt")


def test_log_file_error():
    """Тест записи в файл при ошибке"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    with pytest.raises(ZeroDivisionError):
        function_file_error(10, 0)

    assert os.path.exists("test_log.txt")

    with open("test_log.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        assert "function_file_error error: ZeroDivisionError" in content
        assert "Inputs: (10, 0)" in content

    os.remove("test_log.txt")


def test_log_with_kwargs(capsys):
    """Тест с именованными аргументами"""
    @log()
    def kwargs_func(a: int, b: int, c: int = 0) -> int:
        return a + b + c

    result = kwargs_func(1, 2, c=3)
    assert result == 6

    captured = capsys.readouterr()
    assert "kwargs_func ok" in captured.out


def test_log_error_with_kwargs(capsys):
    """Тест ошибки с именованными аргументами"""
    @log()
    def kwargs_error(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        kwargs_error(5, 0)

    captured = capsys.readouterr()
    assert "kwargs_error error: ZeroDivisionError" in captured.out
    assert "Inputs: (5, 0)" in captured.out