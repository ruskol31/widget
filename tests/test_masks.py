import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert (get_mask_card_number(7000792289606361)) == "7000 79** **** 6361"
    assert (get_mask_card_number(92289606361)) == "Вы неккоректно ввели номер карты"
    assert (get_mask_card_number(123456792289606361)) == "Вы неккоректно ввели номер карты"


def test_get_mask_account():
    assert (get_mask_account(73654108430135874305)) == "**4305"
    assert (get_mask_account(73654108430135874305132)) == "Вы неккоректно ввели номер счета"
    assert (get_mask_account(35874305132)) == "Вы неккоректно ввели номер счета"
