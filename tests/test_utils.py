import json
import pytest
import pandas as pd
from unittest.mock import mock_open, patch
from src.utils import load_operations_list, read_financial_operations, read_financial_operations_exel


def test_load_operations_list_success():
    # Пример данных JSON
    mock_data = json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_operations_list("dummy_path.json")
        assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


def test_load_operations_list_json_decode_error():
    # Некорректные данные JSON
    mock_data = "invalid json"

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_operations_list("dummy_path.json")
        assert result == []


def test_load_operations_list_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_operations_list("dummy_path.json")
        assert result == []


def test_read_financial_operations():
    # Тест на случай корректного файла
    csv_data = ('''id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту''')

    with patch("builtins.open", mock_open(read_data=csv_data)):
        result = read_financial_operations("dummy_path.csv")
        assert result == [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
                           'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
                           'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
                          {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740',
                           'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                           'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}]


def test_read_financial_operations_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_financial_operations("dummy_path.csv")
        assert result == []


def test_read_financial_operations_exel():
    mock_data = pd.DataFrame([
        {
            'id': 650703,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210.0,
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        },
        {
            'id': 3598919,
            'state': 'EXECUTED',
            'date': '2020-12-06T23:00:58Z',
            'amount': 29740.0,
            'currency_name': 'Peso',
            'currency_code': 'COP',
            'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643',
            'description': 'Перевод с карты на карту'
        }
    ])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_financial_operations_exel('dummy_path.xlsx')
        # assert result == [
        #     {
        #         'id': 650703,
        #         'state': 'EXECUTED',
        #         'date': '2023-09-05T11:30:32Z',
        #         'amount': 16210.0,
        #         'currency_name': 'Sol',
        #         'currency_code': 'PEN',
        #         'from': 'Счет 58803664561298323391',
        #         'to': 'Счет 39745660563456619397',
        #         'description': 'Перевод организации'
        #     },
        #     {
        #         'id': 3598919,
        #         'state': 'EXECUTED',
        #         'date': '2020-12-06T23:00:58Z',
        #         'amount': 29740.0,
        #         'currency_name': 'Peso',
        #         'currency_code': 'COP',
        #         'from': 'Discover 3172601889670065',
        #         'to': 'Discover 0720428384694643',
        #         'description': 'Перевод с карты на карту'
        #     }
        # ]
