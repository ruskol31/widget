import os
from dotenv import load_dotenv
import requests

from src.utils import load_operations_list

load_dotenv()

API_KEY = os.getenv('API_KEY') # Замените на ваш API ключ

BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"
# "https://api.apilayer.com/exchangerates_data/convert?to=to&from=from&amount=amount"
def convert_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции, содержащий 'amount' и 'currency'.
    :return: Сумма транзакции в рублях (float).
    """

    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', 'RUB')

    if currency == 'RUB':
        return float(amount)

    try:

        url = "{}?from={}&to=RUB&amount={}".format(BASE_URL, currency, amount)
        response = requests.get(url, headers={'apikey': API_KEY})

        # response = requests.get(BASE_URL, params={
        #     'from': currency,
        #     'to': 'RUB',
        #     'amount': amount
        # }, headers={
        #     'apikey': API_KEY
        # })

        if response.status_code == 200:
            data = response.json()
            return float(data.get('result', 0))
        else:
            print(f"Ошибка при обращении к API: {response.status_code}")
            return 0.0
    except requests.RequestException as e:
        print(f"Ошибка сети: {e}")
        return 0.0

# Пример использования
if __name__ == "__main__":
    opertaion_list = load_operations_list(r'C:\pytnon\widget\data\operations.json')
    # print(opertaion_list)
    for operation in opertaion_list:
        operation_amount = operation.get('operationAmount', {})
        amount = operation_amount.get('amount')
        print("amount=", amount)

        if amount is not None:
            amount = operation['operationAmount']['amount']
            currency = operation["operationAmount"]["currency"]["code"]
            transaction = {'amount': amount, 'currency': currency}
            amount_in_rub = convert_to_rub(transaction)
            print(f"Сумма в рублях: {amount_in_rub}")
        else:
            print("Ключ 'amount' не найден.")

