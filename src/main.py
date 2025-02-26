# from datetime import datetime

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
    print(operation_list)
elif user_input_type_of_data == "2":
    print("пользователь выбрал загрузку из CSV файла")
    operation_list = read_financial_operations(r'C:\pytnon\widget\data\transactions.csv')
    print(operation_list)
elif user_input_type_of_data == "3":
    print("пользователь выбрал загрузку из XLSX файла")
    operation_list = read_financial_operations_exel(r'C:\pytnon\widget\data\transactions_excel.xlsx')
    print(operation_list)
