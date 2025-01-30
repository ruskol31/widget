import logging
from typing import Any


logger = logging.getLogger('masks')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='../logs/masks.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске

def get_mask_card_number(user_input_card_number: Any) -> Any:
    """Принимает на вход номер карты и возвращает ее маску"""

    user_input_card_number = str(user_input_card_number)
    if len(user_input_card_number) == 16:
        logger.info('пользователь правильно ввел номер карты')
        card_number = user_input_card_number.replace(user_input_card_number[6:12], "******")
        mask_card_number = ""
        for i in range(0, len(card_number), 4):
            if i > 0:
                mask_card_number += " "
            mask_card_number += card_number[i : i + 4]

        logger.info('карта замаскирована')
        return mask_card_number
    else:
        logger.error('некорректно ввели номер карты')
        return "Вы некорректно ввели номер карты"


def get_mask_account(user_input_account_number: Any) -> Any:
    """Принимает на вход номер счета возвращает его маску"""
    user_input_account_number = str(user_input_account_number)
    if len(user_input_account_number) == 20:
        user_account_number = user_input_account_number[-6:]
        mask_account = user_account_number.replace(user_account_number[0:2], "**")
        logger.info('счет замаскирован')
        return mask_account
    else:
        logger.error('некорректно ввели номер счета')
        return "Вы некорректно ввели номер счета"
