from unittest.mock import patch, Mock

import requests
from dotenv import load_dotenv

from src.external_api import convert_to_rub, API_KEY

load_dotenv()

def test_convert_to_rub_success():
    # Мок-объект для успешного ответа API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 7500.0}

    with patch('requests.get', return_value=mock_response) as mock_get:
        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        assert result == 7500.0
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?from=USD&to=RUB&amount=100",
            headers={'apikey': API_KEY} # Замените на ваш API ключ
        )

def test_convert_to_rub_error_response():
    # Мок-объект для ответа API с ошибкой
    mock_response = Mock()
    mock_response.status_code = 404

    with patch('requests.get', return_value=mock_response):
        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        assert result == 0.0

def test_convert_to_rub_request_exception():
    # Имитация исключения запроса
    with patch('requests.get', side_effect=requests.RequestException):
        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        assert result == 0.0