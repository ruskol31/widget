import json
import logging
import os
from typing import Any

logger = logging.getLogger('utils')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='../logs/utils.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске
# logger.setLevel(logging.INFO)
#  file_handler = logging.FileHandler('../logs/utils.log')
# file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)

# with open(os.path.dirname(os.path.abspath(__file__))
#           + "/wordbooks/russian_nouns.txt", "r", encoding='utf-8') as file:

def load_operations_list(file_path: str) -> Any:
    '''принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.'''
    try:
        with open(file_path, "r", encoding='utf-8') as operations_file:
            try:
                operations_list = json.load(operations_file)
                logger.info('загрузка файла')
                # print(operations_list)
            except json.JSONDecodeError as ex:
                logger.error(f'произошла ошибка: {ex}')
                print("Ошибка загрузки файла")
                return []
    except FileNotFoundError as ex:
        logger.error(f'произошла ошибка: {ex}')
        print("Файл не найден")
        return []
    # return operations_list
    return operations_list


if __name__ == "__main__":
    # if os.path.exists(file_path):
    # file_path = r'C:\pytnon\widget\data\operations.json'
    #     print('ок')
    # else:
    #     print('путь не найден')
    # load_operations_list(r'C:\pytnon\widget\data\operations.json')
    print(load_operations_list((r'C:\pytnon\widget\data\operations.json')))
