# from datetime import datetime
from src.processing import filter_transactions_by_description
from src.widget import get_date, mask_account_card
from utils import load_operations_list, read_financial_operations, read_financial_operations_exel

# from masks import get_mask_card_number, get_mask_account

# user_input_card_number = input('''Введите номер карты
# - ''')
# print(get_mask_card_number(user_input_card_number))
#
# user_input_account_number = input(''' Введите номер счета
# -''')
# print(get_mask_account(user_input_account_number))

# user_input_account_card_number = input("Введите номер счета или карты")
# print(mask_account_card(user_input_account_card_number))
# print(get_date("2024-03-11T02:26:18.671407"))

print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
user_input_type_of_data = input(f"Выберите необходимый пункт меню: \n"
                                f"1. Получить информацию о транзакциях из JSON-файла\n"
                                f"2. Получить информацию о транзакциях из CSV-файла\n"
                                f"3. Получить информацию о транзакциях из XLSX-файла\n")

if user_input_type_of_data == "1":
    print("пользователь выбрал загрузку из JSON файла")
    operation_list = load_operations_list(r'C:\pytnon\widget\data\operations.json')
elif user_input_type_of_data == "2":
    print("пользователь выбрал загрузку из CSV файла")
    operation_list = read_financial_operations(r'C:\pytnon\widget\data\transactions.csv')
elif user_input_type_of_data == "3":
    print("пользователь выбрал загрузку из XLSX файла")
    operation_list = read_financial_operations_exel(r'C:\pytnon\widget\data\transactions_excel.xlsx')
else:
    print("Неверный выбор")

# print(operation_list)
valid_statuses = {'EXECUTED', 'CANCELED', 'PENDING'}
while True:
    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip().upper()
    if status in valid_statuses:
        break
    print(f"Статус операции \"{status}\" недоступен.")

filtered_transactions = [t for t in operation_list if t['state'].upper() == status]
print(f"Операции отфильтрованы по статусу \"{status}\"")

if not filtered_transactions:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
if sort_choice == 'да':
    order_choice = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
    ascending = order_choice == 'по возрастанию'
    filtered_transactions.sort(key=lambda x: x['date'], reverse=not ascending)

ruble_choice = input("Выводить только рублевые тразакции? Да/Нет\n").strip().lower()
if ruble_choice == 'да':
    filtered_transactions = [t for t in filtered_transactions if t['currency_code'] == 'RUB']

description_choice = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
if description_choice == 'да':
    search_string = input("Введите слово для фильтрации по описанию:\n").strip()
    filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

if not filtered_transactions:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
else:
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    for transaction in filtered_transactions:
        print(f"{transaction['date']} {transaction['description']}")
        print(f"{transaction['from']} -> {transaction['to']}")
        print(f"Сумма: {transaction['amount']} {transaction['currency_code']}\n")
