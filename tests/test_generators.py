import pytest
from src.generators import card_number_generator

@pytest.fixture
def user_data_generator():
    return [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    # {
    #         "id": 142264268,
    #         "state": "EXECUTED",
    #         "date": "2019-04-04T23:20:05.206878",
    #         "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 19708645243227258542",
    #         "to": "Счет 75651667383060284188",
    # },
    ]

def test_filter_by_currency(user_data_generator, currency = "USD"):

    result = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, user_data_generator))
    expected_result = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }]
    assert result == expected_result


def test_transaction_descriptions(user_data_generator):
    result = list((transaction['description'] for transaction in user_data_generator if 'description' in transaction))
    expected_result = ["Перевод организации", "Перевод со счета на счет"]
    assert result == expected_result

@pytest.fixture
def start():
    return 1
@pytest.fixture
def stop():
    return 3
def test_card_number_generator(start, stop):

    generator = card_number_generator(start, stop)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    # expected_result = ["0000 0000 0000 0001, 0000 0000 0000 0002, 0000 0000 0000 0003"]
    # assert result == expected_result



