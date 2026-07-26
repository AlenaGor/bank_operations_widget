"""
Модуль для работы с файлами финансовых операций.
Поддерживает форматы: CSV, Excel (XLSX).
"""

import logging
from pathlib import Path
from typing import List, Dict, Any

import pandas as pd

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler('logs/file_operations.log', mode='w')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает финансовые операции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями

    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: Если файл пустой или имеет неверный формат
    """
    logger.info(f"Начало чтения CSV-файла: {file_path}")

    try:
        # Проверяем существование файла
        path = Path(file_path)
        if not path.exists():
            error_msg = f"Файл не найден: {file_path}"
            logger.error(error_msg)
            raise FileNotFoundError(error_msg)

        # Проверяем размер файла
        if path.stat().st_size == 0:
            error_msg = "Файл пустой"
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Читаем CSV с помощью pandas
        df = pd.read_csv(file_path)

        # Проверяем, что DataFrame не пустой
        if df.empty:
            logger.warning("DataFrame пустой")
            return []

        # Преобразуем в список словарей
        transactions = df.to_dict('records')
        logger.info(f"Успешно прочитано {len(transactions)} транзакций из CSV")
        return transactions

    except pd.errors.EmptyDataError:
        error_msg = "CSV-файл не содержит данных"
        logger.error(error_msg)
        raise ValueError(error_msg)
    except pd.errors.ParserError as e:
        error_msg = f"Ошибка парсинга CSV-файла: {e}"
        logger.error(error_msg)
        raise ValueError(error_msg)
    except Exception as e:
        logger.error(f"Неожиданная ошибка при чтении CSV: {e}")
        raise


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает финансовые операции из Excel-файла (XLSX).

    Args:
        file_path (str): Путь к Excel-файлу

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями

    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: Если файл пустой или имеет неверный формат
    """
    logger.info(f"Начало чтения Excel-файла: {file_path}")

    try:
        # Проверяем существование файла
        path = Path(file_path)
        if not path.exists():
            error_msg = f"Файл не найден: {file_path}"
            logger.error(error_msg)
            raise FileNotFoundError(error_msg)

        # Проверяем размер файла
        if path.stat().st_size == 0:
            error_msg = "Файл пустой"
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Проверяем расширение файла
        if path.suffix.lower() not in ['.xlsx', '.xls']:
            error_msg = (
                f"Неверный формат файла: {path.suffix}. "
                "Ожидается .xlsx или .xls"
            )
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Читаем Excel с помощью pandas
        df = pd.read_excel(file_path)

        # Проверяем, что DataFrame не пустой
        if df.empty:
            logger.warning("DataFrame пустой")
            return []

        # Преобразуем в список словарей
        transactions = df.to_dict('records')
        logger.info(
            f"Успешно прочитано {len(transactions)} транзакций из Excel"
        )
        return transactions

    except pd.errors.EmptyDataError:
        error_msg = "Excel-файл не содержит данных"
        logger.error(error_msg)
        raise ValueError(error_msg)
    except Exception as e:
        logger.error(f"Неожиданная ошибка при чтении Excel: {e}")
        raise
