from typing import Any
def get_mask_card_number(user_input_card_number: Any) -> Any:
    """Принимает на вход номер карты и возвращает ее маску"""

    if len(user_input_card_number) == 16:
        card_number = user_input_card_number.replace(
            user_input_card_number[6:12], "******"
        )
        mask_card_number = ""
        for i in range(0, len(card_number), 4):
            if i > 0:
                mask_card_number += " "
            mask_card_number += card_number[i : i + 4]

        return mask_card_number
    else:
        return "Вы неккоректно ввели номер карты"


def get_mask_account(user_input_account_number: Any) -> Any:
    """Принимает на вход номер счета возвращает его маску"""
    if len(user_input_account_number) == 20:
        user_account_number = user_input_account_number[-6:]
        mask_account = user_account_number.replace[0:2], "**"
        return mask_account
    else:
        return "Вы неккоректно ввели номер счета"
