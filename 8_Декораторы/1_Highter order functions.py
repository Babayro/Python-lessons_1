print('Highter order functions, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
# ЭТО ФУНКЦИИ КОТОРЫЕ МОГУТ ПРИНИМАТЬ В КАЧЕСТВЕ ПАРАМЕТРОВ ДРУГИЕ ФУНКЦИИ ИЛИ ВОЗВРАЩАТЬ ИХ ПОСЛЕ СЛОВА return
def product(n, func):
    result = 1
    for number in range(1, n):
# ЧИСЛО ИЗ ДИПАЗОНА УМНОЖАЕМ НА ЧИСЛО ИЗ ДИАПАЗОНА ПОСЛЕ ТОГО КАК ОНО БУДЕТ УМНОЖЕННО НА САМО СЕБЯ
        result *= func(number)
# ВОЗВРАЩАЕМ В ПЕРЕМЕННУЮ result РЕЗУЛЬТАТ ВЫЧИСЛЕНИЙ 1 * 1 * 2 * 2 * 3 * 3 = 36
    return result
# ФУНКЦИЯ ДЛЯ УМНОЖЕНИЯ ЧИСЛА ИЗ ДИПАЗОНА НА САМО СЕБЯ Т.Е. ВОЗВРАЩАЕТ КВАДРАТ ЧИСЛА, А ПОТОМ УМНОЖАЕМ ЕГО НА СЛЕДУЩЕЕ ЧИСЛО
def square(x):
    return x * x
# ДОБАВЛЯЕМ ФУНКЦИЮ КУБ
def cube(x):
    return x * x * x
# ВПИСЫВАЕМ ДИАПАЗОН И ФУНКЦИЮ УМНОЖЕНИЯ ЧИСЛА САМОГО НА СЕБЯ
print(product(4, square))

# ВЫОДИМ С ФУНКЦИЕЙ КУБ
print(product(4, cube))

# ПРИМЕР С ИСПОЛЬЗОВАНИЕМ ВСТРОЕННОЙ ФУНКЦИИ  sum
# ПАРАМЕТРЫ а и в ДОЛЖНЫ БЫТЬ В ФОРМЕ ОБЪЕКТА СПИСКА Т.К. ИНАЧЕ БУДЕТ ОШИБКА

from random import choice


def my_function(a, b, func):
    result = func([a, b])
    return result

print(my_function(7, 3, sum))

# ПРИМЕР С ДВУМЯ ФУНКЦИЯМИ ВОЗВРАЩАЮЩИМИ СТРОКИ, И ИМПОРТОМ ФУНКЦИИ choice КОТОРАЯ НАХОДИТ ОБЪЕКТ СЛУЧАЙНЫМ ОБРАЗОМ

from random import choice

def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'yeelow')
        color = choice(colors)
        return color
    result = get_color() + ' ' + thing
    return result

print(colorize('apple'))

# МЫ МОЖЕМ ВОЗВРАЩАТЬ НЕ САМ РЕЗУЛЬТАТ, А ФУНКЦИЮ

def make_color():
    def get_color_2():
        colors_2 = ('red', 'green', 'yeelow')
        color_2 = choice(colors_2)
        return color_2
    return get_color_2

first_color = make_color()
print(first_color())

second_color = make_color()
print(first_color())

third_color = make_color()
print(first_color())

# ПОЛУЧАЕМ ДОСТУП ИЗ ВНУТРЕННЕЙ ФУНКЦИИ К ПАРАМЕТРУ ВНЕШНЕЙ ФУНКЦИИ
from random import choice

def colorize_1(thing):
    def get_color():
        colors = ('red', 'green', 'yeelow')
        color_1 = choice(colors)
        return color_1 + ' ' + thing

    return get_color

print(colorize_1('orange')())
colorize_cat = colorize_1('cat')
print(colorize_cat())