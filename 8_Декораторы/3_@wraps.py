print('@wraps РЕЗУЛЬАТ РАБОТЫ ПРОГРАММЫ')

# ДАННЫЙ ДЕКОРАТОР НУЖЕН ДЛЯ СОХРАНЕНИЯ МЕТОДАННЫХ В ФУНКЦИИ
# ИМПОРТИРУЕМ МОДУЛЬ ДЛЯ ПОДРОБНОГО ЧТЕНИЯ ДОКУМЕНТАЦИИ ФУНКЦИЙ
from functools import wraps


def print_function_data(function):
    """
    This is decorator function
    :param function:
    :return:
    """
# ОБОРАЧИВАЕМ НАШУ ФУНКЦИЮ В ДЕКОРАТОР ДЛЯ ПРОСМОТРА ДОКУМЕНТАЦИИ ПРИ ВЫЗОВЕ ФУНКЦИИ help
# БЛАГОДОРЯ ЭТОМУ ДЕКОРАТОРУ МЫ И СОХРАНЯЕМ ВСЕ МЕТОДАННЫЕ НАШЕЙ ФУНКЦИИ!!!
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are using {function.__name__}")
        print(f"Function documentation {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper

@print_function_data
def squares_sum(a, b):
    """

    :param a: first number
    :param b: second number
    :return: sum of squares first and second numbers: (a * a + b * b)
    """
    return a * a + b * b

print(squares_sum(2, 3))


# print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)
print(help(squares_sum))

                                       #    ДОМАШНЕЕ ЗАДАНИЕ

from functools import wraps


def print_args(func): # ВНЕШНЯЯ ЧАСТЬ ЭТО ЗНАЧЕНИЕ КОТОРОЕ МЫ БУДЕМ ПРОВЕРЯТЬ
    @wraps(func) # ВНУТРЕННЯЯ ЧАСТЬ ПРИНИМАЕТ ФУНКЦИЮ КОТОРУЮ МЫ БУДЕМ ДЕКОРИРОВАТЬ
    def wrapper(*args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper


@print_args
def some_func():
    print('Some code')


some_func()