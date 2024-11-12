from src.main import user_input_account_number
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_input_account_card_number):
    '''выделение номера и типа из ввода'''
    parts = user_input_account_card_number.rsplit(' ', 1)
    card_type = parts[0]
    number = parts[1]

    # проверка типа ввода и выбор соответствующей маскировки #
    if card_type in ['Visa', 'Maestro']:
        #приминение маски для карт#
        masked_number = get_mask_card_number(number)
    elif card_type == 'Счет':
        # выбор маскировки для счетов#
        masked_number = get_mask_account(number)
    else:
        return "Неизвестный тип карты или счета"

    return f"{card_type} {masked_number}"
