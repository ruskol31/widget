# from functools import wraps
# def wrapped(function):
#     @wraps(function)
#     def inner(arg):
#         return function(arg)
#     return inner


import functools
import logging
from typing import Any


def log(filename: str = "mylog.txt") -> Any:
    """Ожидаемый вывод в лог-файл mylog.txt my_function ok, result =
    Ожидаемый вывод при ошибке:
    my_function error: тип ошибки. Inputs: (1, 2), {}"""

    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format="%(asctime)s - %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    def decorator(func: Any) -> Any:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            try:
                # logging.info(f"Начало выполнения функции: {func_name} с аргументами: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"{func_name} ок, result ={result}")
                return result
            except Exception as e:
                logging.error(f"{func_name} error: тип ошибки: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
