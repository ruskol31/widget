import json
import logging
# import os
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


import csv


def read_financial_operations(file_path):
    '''принимает на вход путь до JSON-файла и
        возвращает список словарей с данными о финансовых транзакциях.'''
    operations = []

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            try:
                csv_reader = csv.DictReader(file, delimiter=';')

                for row in csv_reader:
                    operation = {
                    'id': row['id'],
                    'state': row['state'],
                    'date': row['date'],
                    'amount': row['amount'],
                    'currency_name': row['currency_name'],
                    'currency_code': row['currency_code'],
                    'from': row['from'],
                    'to': row['to'],
                    'description': row['description']
                     }
                    operations.append(operation)
            except Exception as ex:
                logger.error(f'произошла ошибка: {ex}')
                print("Ошибка загрузки файла")
    except FileNotFoundError as ex:
        logger.error(f'произошла ошибка: {ex}')
        print("Файл не найден")
        return []
    return operations


if __name__ == "__main__":
    # if os.path.exists(file_path):
    # file_path = r'C:\pytnon\widget\data\operations.json'
    #     print('ок')
    # else:
    #     print('путь не найден')
    # load_operations_list(r'C:\pytnon\widget\data\operations.json')
    # print(load_operations_list((r'C:\pytnon\widget\data\operations.json')))

    operations = read_financial_operations(r'C:\pytnon\widget\data\transactions.csv')
    print(operations)
    # for op in operations:
    #     print(f"ID: {op['id']}, State: {op['state']}, Date: {op['date']}, Amount: {op['amount']}, "
    #           f"Currency: {op['currency_name']} ({op['currency_code']}), From: {op['from']}, "
    #           f"To: {op['to']}, Description: {op['description']}")
