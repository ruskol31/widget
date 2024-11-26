import pytest
from src.widget import mask_account_card

# @pytest.fixture
# def fixture_name():
#     return

@pytest.mark.parametrize ('user_input_account_card_number, expected', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('Visa 152436', 'Visa Вы некорректно ввели номер карты'),
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Maest 1596837868705199', 'Неизвестный тип карты или счета')
])
def test_mask_account_card(user_input_account_card_number, expected):
    assert mask_account_card(user_input_account_card_number) == expected

    # "2024-03-11T02:26:18.671407"