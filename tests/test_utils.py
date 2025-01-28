import json
import pytest
from unittest.mock import mock_open, patch
from src.utils import load_operations_list


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

