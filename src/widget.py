# from src.main import user_input_account_number
from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number
from typing import Any


def mask_account_card(user_input_account_card_number: Any) ->Any:
    """выделение номера и типа из ввода"""
    parts = user_input_account_card_number.rsplit(" ", 1)
    card_type = parts[0]
    number = parts[-1]

    # проверка типа ввода и выбор соответствующей маскировки #
    if card_type in ["Visa", "Maestro", "Visa Platinum"]:
        # применение маски для карт#
        masked_number = get_mask_card_number(number)
    elif card_type == "Счет":
        # выбор маскировки для счетов#
        masked_number = get_mask_account(number)
    else:
        return "Неизвестный тип карты или счета"

    return f"{card_type} {masked_number}"


def get_date(date_string):
    from datetime import datetime

    date = datetime.fromisoformat(date_string)
    return date.strftime("%d.%m.%Y")
