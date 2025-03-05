from datetime import datetime
import re
from collections import defaultdict


# from typing import Dict, List, Optional


def filter_by_state(list_of_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """оставлет только операции с заданным статусом"""

    return [item for item in list_of_operation if item.get("state") == state]


def parse_date(date_str):
    """
    Преобразует строку даты в объект datetime, поддерживая несколько форматов.

    :param date_str: Строка даты.
    :return: Объект datetime.
    """
    date_formats = [
        "%Y-%m-%dT%H:%M:%SZ",  # Формат с 'Z' в конце
        "%Y-%m-%dT%H:%M:%S.%f"  # Формат с миллисекундами
    ]

    for date_format in date_formats:
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError:
            continue

    raise ValueError(f"Не удалось распознать формат даты: {date_str}")


def sort_by_date(transactions, ascending=True):
    """
    Сортирует список транзакций по дате.

    :param transactions: Список словарей с данными о транзакциях.
    :param ascending: Булево значение, определяющее порядок сортировки (по возрастанию или убыванию).
    :return: Отсортированный список транзакций.
    """
    sorted_transactions = sorted(
        transactions,
        key=lambda x: parse_date(x['date']),
        reverse=not ascending
    )

    return sorted_transactions


# def sort_by_date(list_of_operation: list[dict], order: str = "descending") -> list[dict]:
#     """сортирует список операций от последней по убыванию даты"""
#
#     # sorted_data = sorted(
#     #     list_of_operation,
#     #     key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%SZ"),
#     #     reverse=(order.lower() == "descending"),
#     # )
#     sorted_data = list_of_operation.sort(key=lambda x: x['date'], reverse=not 'ascending')
#     return sorted_data

#
# list_of_operation = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
# list_of_executed_operation = filter_by_state(list_of_operation)
# sorted_list_of_operation = sort_by_date(list_of_operation)
# print("список по убыванию даты", sorted_list_of_operation)
# print("список выполненных операций", list_of_executed_operation)


def filter_transactions_by_description(operation_list: list[dict], search_string: str) -> list[dict]:
    """
    Фильтрует список банковских операций, возвращая только те, в описании которых содержится заданная строка.

    :param operation_list: Список словарей с данными о банковских операциях.
    :param search_string: Строка поиска для фильтрации по описанию.
    :return: Список словарей, соответствующих критерию поиска.
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [t for t in operation_list if pattern.search(t.get('description', ''))]


def count_transactions_by_category(operation_list, categories):
    """
    Подсчитывает количество операций в каждой категории, используя регулярные выражения.

    :param operation_list:
    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий операций.
    :return: Словарь, где ключи — это названия категорий, а значения — количество операций в каждой категории.
    """
    category_count = defaultdict(int)

    for operation in operation_list:
        description = operation.get('description', '').lower()
        for category in categories:
            # Создаем регулярное выражение для поиска категории в описании
            pattern = re.compile(re.escape(category), re.IGNORECASE)
            if pattern.search(description):
                category_count[category] += 1

    return dict(category_count)
