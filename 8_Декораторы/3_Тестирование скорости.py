print('ТЕСТИРОВАНИЕ СКОРОСТИ, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
# ИМПОРТИРУЕМ НЕ ВЕСЬ МОДУЛЬ time, А ТОЛЬКО ФУНКЦИЮ time
from time import time
# ИМПОРТИРУЕМ wraps ДЛЯ ОБЁРТКИ ДОКУМЕНТАЦИИ
from functools import wraps
                               # ФУНКЦИЯ ДЕКОРАТОР
def speed_test(function):
    @wraps(function)
# args и  kwargs ВПИСЫВАЕМ ДЛЯ ХОРОШЕГО ТОНА, ЧТОБ ЕСЛИ ЗАХОТИМ МОЖНО БЫЛО ИХ ИСПОЛЬЗЫВАТЬ
    def wrapper(*args, **kwargs):
# В ПЕРЕМЕННУЮ НАЧАЛЬНО ВРЕМЕНИ ЗАПИСЫВАЕМ ФУНКЦИЮ time
        start_time = time()
# В ПЕРЕМЕННОЙ РЕЗУЛЬАТ БУДЕТ НАХОДИТСЯ ФУНКЦИОНАЛ НИЖНЕЙ ЗАДЕКОРИРОВАННОЙ ФУНКЦИИ
        result = function(*args, **kwargs)
# КОНЕЧНОЕ ВРЕМЯ
        end_time = time()
# РЕЗУЛЬТАТ КОНЕЧНОЕ ВРЕМЯ МИНУС СТАРТОВОЕ ВРЕМЯ ВОЗВРАЩАЕТСЯ В ПЕРЕМЕННУЮ result
        print(f"Time of code execution {end_time - start_time}")
        return result
#  ВОЗВРАЩАЕМ ДОКУМЕТАЦИЮ С МЕТОДАННЫМИ
    return wrapper

# ДЕКОРИРУЕМ ФУНКЦИЮ
@speed_test
def sum_with_list():
    return sum([number for number in range(10000000)])
# ПОЛУЧАЕМ ВРЕМЯ
sum_with_list()
# ПОЛУЧАЕМ СУММУ ВСЕХ ИТЕРАЦИЙ В ДИАПАЗОНЕ
print(sum_with_list())

# ИСПОЛЬЗУЕМ ГЕНЕРАТОР ФУНКЦИЙ ДЛЯ УМЕНЬШЕНИЯ ВРЕМЕНЕ ОБРАБОТКИ ДИАПАЗОНА ПОЧТИ В ДВА РАЗА
def sum_with_gen():
    return sum([number for number in range(10000000)])
print(sum_with_gen())

# ДАННУЮ ФУНКЦИЮ ДЛЯ ИЗМЕРЕНИЯ СКОРОСТИ МОЖНО ПРИМЕНЯТЬ ДЛЯ ЛЮБОЙ ФУНКЦИИ

                                         # ДОМАШНЕЕ ЗАДАНИЕ
from functools import wraps


def hello_from_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result) + ' Hello from decorator!'
    return wrapper


@hello_from_decorator
def some_func():
    return 3


print(some_func())
