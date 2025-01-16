import json
import os
from typing import Any


# with open(os.path.dirname(os.path.abspath(__file__))
#           + "/wordbooks/russian_nouns.txt", "r", encoding='utf-8') as file:

def load_operations_list(file_path: str) -> Any:
    '''принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.'''
    try:
        with open(file_path, "r", encoding='utf-8') as operations_file:
            try:
                operations_list = json.load(operations_file)
                # print(operations_list)
            except json.JSONDecodeError:
                print("Ошибка загрузки файла")
                return []
    except FileNotFoundError:
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
