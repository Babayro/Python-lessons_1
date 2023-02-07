print('ПРОВЕРКА АРГУМЕНТОВ, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')

# С ПОМОЩЬЮ ДЕКОРАТОРА МОЖНО ВЫБРАСЫВАТЬ ОШИБКУ ИЛИ ВЫХОДИТЬ ИЗ ФУНКЦИИ ПРИ ПЕРЕДАЧИ ОПРЕДЕЛЁННОГО ТИПА АРГУМЕНТОВ
from functools import wraps

def prohibit_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('KEyword arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper
# СТОИТ НАМ ЗАДЕКОРИРОВАТЬ И ВЫЗВАТЬ ФУНКЦИЮ С КЛЮЧОМ ТО ДЕКОРАТОР ВЫКИНЕТ ОШИБКУ
#@prohibit_kwargs
def print_hello(name):
    print(f'Hello {name}!')

print_hello(name='Jack')

# ФУНКЦИЯ ДЕКОРАТОР ВЫДАЮЩАЯ ОШИБКУ ПРИ integer

def prohibit_int_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper
# СТОИТ НАМ ЗАДЕКОРИРОВАТЬ И ВЫЗВАТЬ ФУНКЦИЮ С КЛЮЧОМ ТО ДЕКОРАТОР ВЫКИНЕТ ОШИБКУ
@prohibit_int_arguments
def print_not_int(int):
    print(f'Hello int {int}!')


print_not_int(3)

                                   # ДОМАШНЕЕ ЗАДАНИЕ



from functools import wraps


def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return func(*args, **kwargs)
        else:
            raise ValueError('Function must have less than 3 arguments!')
    return wrapper


@prohibit_more_than_2_args
def some_func(a, b, c):
    return 'Hi'


print(some_func(1, 2, 3))