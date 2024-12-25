import pytest
import logging
from src.decorators import log


@log(filename=None)
def my_function(x, y):
    return x + y


def test_my_function(caplog):
    with caplog.at_level(logging.INFO):
        result = my_function(1, 2)
        assert result == 3
        assert "my_function ок, result =3" in caplog.text


def test_my_function(caplog):
    with caplog.at_level(logging.ERROR):
        with pytest.raises(TypeError):
            my_function(1, 2, 3)
        assert "my_function error: тип ошибки: TypeError. Inputs: (1, 2, 3), {}" in caplog.text
