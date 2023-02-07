print('ДЕКОРАТОРЫ С АРГУМЕНТАМИ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
# СОЗДАЁМ ДЕКОРАТОР КОТОРЫЙ БУДЕТ ПРОВЕРЯТЬ ПЕРВЫЙ АРГУМЕНТ ДИКОРИРУЕМОЙ ФУНКЦИИ

from functools import wraps

# СОЗДАЁМ ФУНКЦИЮ ДЕКОРАТОР
# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции


def check_if_first_arg_is(value):# ФУНКЦИЯ КОТОРАЯ БУДЕТ ПРИНИМАТЬ ЗНАЧЕНИЕ
    def inner_dec(func):  # ФУНКЦИЯ КОТОРАЯ БУДЕТ ПРИНИМАТЬ В КАЧЕТСВЕ АРГУМЕНТА ДЕКОРИРУЕМУЮ ФУНКЦИЮ
        @wraps(func)
        def wrapper(*args, **kwargs): # аргументы прибывают отсюда
            if args and args[0] != value:# ЕСЛИ ВООБЩЕ ЕСТЬ args ТО ВЫПОЛНЯЕМ ДЕЙСТВИЯ
                print(f'First argument has to be {value}')
            return func(*args, **kwargs)
        return wrapper
    return inner_dec



@check_if_first_arg_is('fi')
def print_rainbow_colors(*colors):
    print(colors)

print_rainbow_colors('red', 'yellow', 'green', 'indigo', 'violet', 'blue', 'orange')


@check_if_first_arg_is('7')
def multiply_7(a, b):
    return a*b

print(multiply_7(7, 3))

# СОЗДАЁМ ФУНКЦИЮ ДЕКОРАТОР
# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции

def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):# аргументы прибывают отсюда
            new_args = []#5 ДОБАВЛЯЕМ В СПИСОК
            for a, t in zip(args, types): #3 ПРИ ПОМОЩИ zip МЫ СОПОСТАВЛЯЕМ ДЛЯ КАЖДОГО ЭЛЕМЕНТА args ЭЛЕМЕНТ type
                new_args.append(t(a))#4 ПРИВОДИМ К ЭТОМУ ТИПУ И ДОБАВЛЯЕМ В НОВЫЙ СПИСОК
            return func(*new_args, **kwargs)
        return wrapper
    return inner_dec

@enforce(str, int) # ПРЕОБРАЗУЕТ СТРОКУ '5' В int
def print_text_n_times(text, n):#2 ТАКЖЕ ПРЕДАЁМ ПАРАМЕТЫ В ФОРМЕ КОРТЕЖА
    for number in range(n):
        print(text)

print_text_n_times('Hi!', '5')#1 ИЗНАЧАЛЬНО У НАС СУЩЕСТВУЕТ args в ФОРМЕ КОРТЕЖА

@enforce(float, float)
def divide(a, b):
    return a/b
print(divide(4, 2))
print(divide('4', '2')) # БЛАГОДАРЯ ДЕКОРАТОРУ, МЫ ПЕРЕВОДИМ string B int

                             #ПРИМЕР 2
                    # ПЕРЕДАЧА АРГУМЕНТОВ В ДЕКОРИРУЕМОЮ ФУНКЦИЮ.
def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):  # аргументы прибывают отсюда
        print("Смотри, что я получил:", arg1, arg2)
        function_to_decorate(arg1, arg2)

    return a_wrapper_accepting_arguments


# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("Меня зовут", first_name, last_name)


print_full_name("Питер", "Венкман")
# выведет:
# Смотри, что я получил: Питер Венкман
# Меня зовут Питер Венкман
# *

                              # ПРИМЕР 3
                        # ДЕКОРИРОВАНИЕ МЕТОДОВ
# Один из важных фактов, которые следует понимать, заключается в том,
# что функции и методы в Python'e — это практически одно и то же, за исключением того,
# что методы всегда ожидают первым параметром ссылку на сам объект (self).
# Это значит, что мы можем создавать декораторы для методов так же, как и для функций, просто не забывая про self.

def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3  # действительно, дружелюбно - снизим возраст ещё сильней :-)
        return method_to_decorate(self, lie)

    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("Мне %s, а ты бы сколько дал?" % (self.age + lie))


l = Lucy()
l.sayYourAge(-3)
# выведет: Мне 26, а ты бы сколько дал?
