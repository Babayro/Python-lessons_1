print('ЗНАКОСТВО С ДЕКОРАТОРАМИ, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')

# КОГДА МЫ ХОТИМ РАСШИРИТЬ ФУНКЦИОНАЛ ФУНКЦИИ МЫ МОЖЕМ ПРИМЕНЯТЬ ДЕКОРАТОРЫ
# ДАННАЯ ФУНКЦИЯ БЕЗ ПЕРЕДАЧИ АРГУМЕНТА
# def simple_function():
#     # print('Some code before the old code')
#     print('Simple code')
#     # print(Some code after the old code)
#
# simple_function()

def decorator_function(original_function):
    def wrap_function():
        print('Some code before the old code')
        original_function()
        print('Some code after the old code')
    return wrap_function
#
# decorated_function = decorator_function(simple_function)
#
# decorated_function()
#
#                             !!! ДАННАЯ ФУНКЦИЯ БЕЗ ПЕРЕДАЧИ АРГУМЕНТА !!!
# ВКЛЮЧАЕМ ДЕКОРАТОР, БЕЗ ВКЛЮЧЕНИЯ ВЫВЕДЕТСЯ ТОЛЬКО simple_function
# ДЕКОРАТОР ЗАВОРАЧИВАЕТ ВЫШЕПРЕВЕДЁННУЮ ФУНКЦИЮ В НИЖНЮЮ, КАК В ОБЁРТКУ
@ decorator_function
def simple_function():
    print('Simple function code')

simple_function()
                            # !!! ФУНКЦИЯ С ПЕРЕДАЧЕЙ АРГУМЕНТОВ !!!

def make_compliment(func):
    def wrapper(*args, **kwargs):
        print('Nice to meet you')
        func(*args, **kwargs)
        print('You look great!')
    return wrapper

@make_compliment
def ask_name():
    print('Whot is your name?')

ask_name()

@make_compliment
def say_name(name):
    print('My name is ' + name)

say_name('Jack')

@make_compliment
def order(food, drink):
    print(f'Give me {food} and {drink}')

order(food='chips', drink='kola')
