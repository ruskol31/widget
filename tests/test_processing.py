import pytest
import unittest
from src.processing import filter_by_state, sort_by_date, filter_transactions_by_description


@pytest.fixture
def user_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(user_data):
    assert filter_by_state(user_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date(user_data):
    assert sort_by_date(user_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sample_transactions():
    return [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 1000.0,
            'currency_name': 'Ruble',
            'currency_code': 'RUB',
            'from': 'Account 1',
            'to': 'Account 2',
            'description': 'Перевод организации'
        },
        {
            'id': 2,
            'state': 'CANCELED',
            'date': '2023-09-06T11:30:32Z',
            'amount': 2000.0,
            'currency_name': 'Dollar',
            'currency_code': 'USD',
            'from': 'Account 3',
            'to': 'Account 4',
            'description': 'Оплата услуг'
        },
        {
            'id': 3,
            'state': 'PENDING',
            'date': '2023-09-07T11:30:32Z',
            'amount': 3000.0,
            'currency_name': 'Euro',
            'currency_code': 'EUR',
            'from': 'Account 5',
            'to': 'Account 6',
            'description': 'Перевод с карты на карту'
        }
    ]


def test_filter_transactions_by_description(sample_transactions):
    # Тестируем фильтрацию по описанию
    result = filter_transactions_by_description(sample_transactions, 'перевод')
    assert len(result) == 2
    assert result[0]['id'] == 1
    assert result[1]['id'] == 3
