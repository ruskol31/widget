# from datetime import datetime
from src.widget import get_date, mask_account_card

# from masks import get_mask_card_number, get_mask_account

# user_input_card_number = input('''Введите номер карты
# - ''')
# print(get_mask_card_number(user_input_card_number))
#
# user_input_account_number = input(''' Введите номер счета
# -''')
# print(get_mask_account(user_input_account_number))

user_input_account_card_number = input("Введите номер счета или карты")
print(mask_account_card(user_input_account_card_number))
print(get_date("2024-03-11T02:26:18.671407"))
