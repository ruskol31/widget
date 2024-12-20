# from functools import wraps
# def wrapped(function):
#     @wraps(function)
#     def inner(arg):
#         return function(arg)
#     return inner


import functools
import logging

def log(filename=None):
    # Настройка логирования
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format='%(asctime)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            try:
                # logging.info(f"Начало выполнения функции: {func_name} с аргументами: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"{func_name} ок")
                return result
            except Exception as e:
                logging.error(f"{func_name} error: тип ошибки: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
        return wrapper
    return decorator

@log(filename= None)
def my_function(x, y):
    return x + y

my_function(1, 2)

# Ожидаемый вывод в лог-файл
# mylog.txt
#  при успешном выполнении:
#
# my_function ok
#
# Ожидаемый вывод при ошибке:
#
# my_function error: тип ошибки. Inputs: (1, 2), {}
#
# Где
# тип ошибки
#  заменяется на текст ошибки.