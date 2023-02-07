print('Generator functions, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
# Generators are iterators
# Generators can be created with generator functions
# Generators can be created with generator expressions

# FUNCTION RETURNING IN VALUE
# ГЕНЕРАТОР ЯВЛЯЕТСЯ ИТЕРАТОРОМ
def my_function(x):
    return x
# print(my_function(4))

def count_up_to(x):
    count = 1
 # ПОКА  count МЕНЬШЕ ИЛИ РАВНО ИКС МЫ УВЕЛИЧИВАЕМ ЕГО ЗНАЧЕНИЕ ПОСРЕДСТВОМ ИТЕРАЦИЙ С 1 И ДО УКАЗАННОГО НАМИ ПРИ ВЫЗОВЕ ФУНКЦИИ
    while count <= x:
# ФУНКЦИЯ yield ВЫРАБАТЫВАЕТ ЗНАЧЕНИЯ И НЕ ОБНУЛЯЕТСЯ ПОСЛЕ ИТЕРАЦИИ, ТАКЖЕ КАК И next ЗАСЫПАЕТ ПОСЛЕ ПЕРВОЙ И ПОСЛЕДУЮЩИХ ИТЕРАЦИЙ
# ПРИ ЗАСЫПАНИИ ОНА ЗАПОМИНАЕТ ПОСЛЕДНЕЕ ЗНАЧЕНИЕ, И ДАЛЕЕ РАБОТА БУДЕТ НАЧАТА НЕ С 0, А С ЗАПОМНИННОГО СОСТОЯНИЯ
        yield count
        count += 1

# print(count_up_to(4))
# ДАННЫЙ ОБЪЕКТ ЗАПИСЫВАЕМ В ПЕРЕМЕННУЮ ИТЕРАТОР
counter = count_up_to(1)
# ДЛЯ ИТЕРАЦИЙ ИСПОЛЬЗУЕМ МЕТОД ИЛИ ФУНКЦИЮ NEXT
print(counter.__next__())
# print(next(counter))

for number in count_up_to(10):
    print(number)

                                                    # ДОМАШНЕЕ ЗАДАНИЕ
                                                    # ЗАДАЧА 1

def get_week_day():
    week = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    for day in week:
        yield day

current_day = get_week_day()
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())

                                     # ЗАДАЧА  2
def even_odd():
    value = 'even'
    while True:
        yield value
        if value == 'even':
            value = "odd"
        else:
            value = "even"

even_odd_generator = even_odd()

print(next(even_odd_generator))

print(next(even_odd_generator))

print(next(even_odd_generator))

print(next(even_odd_generator))


