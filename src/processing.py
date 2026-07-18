"""
Модуль для обработки данных банковских операций
"""
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/processing.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по значению ключа 'state'.
    """
    logger.info(f"Фильтрация операций по статусу: {state}")

    result = [op for op in operations if op.get('state') == state]

    logger.debug(f"Найдено {len(result)} операций с статусом {state}")
    return result


def sort_by_date(operations: List[Dict[str, Any]], is_descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.
    """
    logger.info(f"Сортировка операций по дате, порядок: {'убывание' if is_descending else 'возрастание'}")

    result = sorted(operations, key=lambda x: x.get('date', ''), reverse=is_descending)
    logger.debug(f"Отсортировано {len(result)} операций")
    return result