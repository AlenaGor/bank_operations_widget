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

    # Подсчет статистики по категориям
    categories = ['Перевод', 'Оплата', 'Пополнение']
    category_counts = count_categories(filtered_transactions, categories)
    print(f"\n📊 Статистика по категориям:")
    for category, count in category_counts.items():
        print(f"   {category}: {count}")

    print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")

    for transaction in filtered_transactions:
        print(format_transaction(transaction))