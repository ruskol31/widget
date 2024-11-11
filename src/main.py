from masks import get_mask_card_number, get_mask_account

user_input_card_number = input('''Введите номер карты
- ''')
print(get_mask_card_number(user_input_card_number))

user_input_account_number = input(''' Введите номер счета
-''')
print(get_mask_account(user_input_account_number))



