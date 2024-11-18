from datetime import datetime


def filter_by_state(list_of_operation: list, state= "EXECUTED") -> list:
    '''оставлет только операции с заданным статусом'''

    return [item for item in list_of_operation if item.get("state") == state]


def sort_by_date(list_of_operation: list, order="descending") -> list:
    '''сортирует список операций от последней по убыванию даты'''

    sorted_data = sorted(
        list_of_operation,
        key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=(order.lower() == "descending"),
    )

    return sorted_data


list_of_operation = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

list_of_executed_operation = filter_by_state(list_of_operation)
sorted_list_of_operation = sort_by_date(list_of_operation)
print("список по убыванию даты", sorted_list_of_operation)
print("список выполненных операций", list_of_executed_operation)
