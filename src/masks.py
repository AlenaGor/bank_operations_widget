"""
Модуль для маскировки номеров карт и счетов
"""
import logging

# Настройка логгера для модуля masks
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаём файловый handler
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Создаём форматтер
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем handler к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Args:
        card_number: Номер карты (16 цифр)

    Returns:
        Замаскированный номер карты в формате XXXX XX** **** XXXX
    """
    logger.info(f"Маскировка номера карты: {card_number[:4]}...{card_number[-4:]}")

    if not card_number.isdigit() or len(card_number) != 16:
        error_msg = f"Некорректный номер карты: {card_number} (должен содержать 16 цифр)"
        logger.error(error_msg)
        raise ValueError("Номер карты должен содержать 16 цифр")

    result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.debug(f"Успешно замаскирован номер карты: {result}")
    return result


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    Args:
        account_number: Номер счета

    Returns:
        Замаскированный номер счета в формате **XXXX
    """
    logger.info(f"Маскировка номера счета: ...{account_number[-4:]}")

    if not account_number.isdigit() or len(account_number) < 4:
        error_msg = f"Некорректный номер счета: {account_number} (должен содержать минимум 4 цифры)"
        logger.error(error_msg)
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    result = f"**{account_number[-4:]}"
    logger.debug(f"Успешно замаскирован номер счета: {result}")
    return result