"""
Главный модуль программы для работы с банковскими операциями.
"""

import sys
from pathlib import Path

# Добавляем путь к проекту
sys.path.insert(0, str(Path(__file__).parent))

from src.utils import get_transactions_from_json
from src.file_operations import read_csv_transactions, read_excel_transactions
from src.processing import filter_by_state, sort_by_date
from src.filtering import filter_by_description
from src.category_counter import count_categories
from src.masks import mask_account_card
from src.widget import get_date


def get_user_choice(prompt: str, options: list) -> str:
    """
    Получает выбор пользователя из списка вариантов.

    Args:
        prompt: Текст приглашения
        options: Список допустимых вариантов

    Returns:
        str: Выбранный пользователем вариант
    """
    while True:
        choice = input(prompt).strip().lower()
        if choice in [opt.lower() for opt in options]:
            return choice
        print(f"Неверный ввод. Доступные варианты: {', '.join(options)}")


def get_user_status(valid_statuses: list) -> str:
    """
    Получает от пользователя статус для фильтрации.

    Args:
        valid_statuses: Список допустимых статусов

    Returns:
        str: Выбранный статус в верхнем регистре
    """
    valid_statuses_lower = [s.lower() for s in valid_statuses]

    while True:
        status = input(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}\n"
        ).strip()

        if status.lower() in valid_statuses_lower:
            return status.upper()

        print(f'Статус операции "{status}" недоступен.\n')


def format_transaction(transaction: dict) -> str:
    """
    Форматирует одну транзакцию для вывода.

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        str: Отформатированная строка транзакции
    """
    date = get_date(transaction.get('date', ''))
    description = transaction.get('description', 'Нет описания')

    amount = transaction.get('operationAmount', {})
    amount_value = amount.get('amount', '0')
    currency = amount.get('currency', {}).get('name', 'руб.')

    from_field = transaction.get('from', '')
    to_field = transaction.get('to', '')

    from_masked = mask_account_card(from_field) if from_field else ''
    to_masked = mask_account_card(to_field) if to_field else ''

    result = f"\n{date} {description}"
    if from_masked and to_masked:
        result += f"\n{from_masked} -> {to_masked}"
    elif to_masked:
        result += f"\n{to_masked}"
    elif from_masked:
        result += f"\n{from_masked}"

    result += f"\nСумма: {amount_value} {currency}"

    return result


def main():
    """Главная функция программы."""
    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("\nВаш выбор: ").strip()

    transactions = []

    if choice == '1':
        file_path = 'data/operations.json'
        print("\nДля обработки выбран JSON-файл.")
        transactions = get_transactions_from_json(file_path)
    elif choice == '2':
        file_path = 'data/transactions.csv'
        print("\nДля обработки выбран CSV-файл.")
        transactions = read_csv_transactions(file_path)
    elif choice == '3':
        file_path = 'data/transactions_excel.xlsx'
        print("\nДля обработки выбран XLSX-файл.")
        transactions = read_excel_transactions(file_path)
    else:
        print("Неверный выбор. Завершение программы.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции.")
        return

    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    status = get_user_status(valid_statuses)

    filtered_transactions = filter_by_state(transactions, status)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nОперации отфильтрованы по статусу \"{status}\"")

    sort_choice = get_user_choice(
        "\nОтсортировать операции по дате? (Да/Нет): ",
        ['да', 'нет']
    )

    if sort_choice == 'да':
        order_choice = get_user_choice(
            "Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): ",
            ['по возрастанию', 'по убыванию']
        )
        is_descending = order_choice == 'по убыванию'
        filtered_transactions = sort_by_date(filtered_transactions, is_descending)

    rub_choice = get_user_choice(
        "\nВыводить только рублевые транзакции? (Да/Нет): ",
        ['да', 'нет']
    )

    if rub_choice == 'да':
        filtered_transactions = [
            t for t in filtered_transactions
            if t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB'
        ]

    desc_choice = get_user_choice(
        "\nОтфильтровать список транзакций по определенному слову в описании? (Да/Нет): ",
        ['да', 'нет']
    )

    if desc_choice == 'да':
        search_word = input("Введите слово для поиска: ").strip()
        filtered_transactions = filter_by_description(filtered_transactions, search_word)

    if not filtered_transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")

    for transaction in filtered_transactions:
        print(format_transaction(transaction))


if __name__ == "__main__":
    main()