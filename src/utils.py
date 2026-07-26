"""
Модуль для работы с файлами
"""
import json
import logging
from typing import List, Dict, Any

# Настройка логгера для модуля utils
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаём файловый handler
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Создаём форматтер
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем handler к логгеру
logger.addHandler(file_handler)


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.

    Args:
        file_path: Путь к JSON-файлу

    Returns:
        Список словарей с данными о транзакциях.
        Если файл пустой, содержит не-список или не найден — возвращает пустой список.
    """
    logger.info(f"Попытка открыть файл: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            logger.debug(f"Файл успешно прочитан: {file_path}")

            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
                return data
            else:
                logger.error(f"Файл {file_path} содержит не список, а {type(data).__name__}")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON в файле {file_path}: {e}")
        return []
    except Exception as e:
        logger.error(f"Неизвестная ошибка при чтении файла {file_path}: {e}")
        return []