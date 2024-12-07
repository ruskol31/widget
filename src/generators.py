def filter_by_currency(transactions: list[dict], currency: str = "USD") -> iter:
    #     return (item for item in transactions if item.get("name") == "USD")

    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions: list[dict]) -> iter:
    description = (transaction['description'] for transaction in transactions if 'description' in transaction)
    for x in description:
        yield x

def card_number_generator(start, end):
    for number in range(start, end + 1):
        card_number = f"{number:016}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number


transactions = [
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
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
descriptions = transaction_descriptions(transactions)
for _ in range(2):
    print(next(descriptions))

for card_number in card_number_generator(1, 5):
    print(card_number)

