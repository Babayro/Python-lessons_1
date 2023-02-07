операторы = 'НЕКОТОРЫЕ ЧАСТО ИСПОЛЬЗУЕМЫЕ ФУНКЦИИ И ОПЕРАТОРЫ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(операторы)
# range (ДИАПАЗОН) ГЕНЕРАТОР ПОСЛЕДОВАТЕЛЬНОСТЕЙ
# С КАКОГО ПО КАКОЕ, ШАГ
for x in range(3, 11, 2):
    print(x)

# ПОЛУЧАЕМ ОБЪЕКТ range(0,5) НЕ ИМЕЕТ ОТНОШЕНИЕ К ВЕРХНЕМУ ЦИКЛУ
print(range(5))
# ВЫВОД СПИСКА ИЗ ПЯТИ ЭЛЕМЕНТОВ НАЧИНАЯ С 0, Т.К. ОТСЧЁТ ВСЕГДА НАЧИНАЕТСЯ С 0
print(list(range(5)))

# РАСПЕЧАТКА ИНДЕКСОВ ОПРЕДЕЛЁННОЙ ПОСЛЕДОВАТЕЛЬНОСТИ (a is at index 0)
index_letter = 0
my_string = 'apokfgeprotiy'
for letter in my_string:
    print(letter + ' is at index ' + str(index_letter) )
    index_letter = index_letter + 1

# РАСПЕЧАТКА ИНДЕКСОВ ПРИ ПОМОЩИ ФУНКЦИИ enumerate (0, 'a') ПОЛУЧАЕМ ОБЪЕКТЫ ТИПА tuple
my_string = 'apokfgeprotiy'
for item in enumerate(my_string):
    print(item)
# БОЛЕЕ УКОРОЧЕННАЯ ЗАПИСЬ
my_string = 'jhiygytdtd'
for index, letter in enumerate(my_string):
    print(letter + ' is at index ' + str(index))
# in КАК В ЦИКЛЕ for, МЫ МОЖЕМ ПРОВЕРЯТЬ НАХОДИТСЯ ЛИ ЗНАЧЕНИЕ В КАКОЙ ЛИБО ПОСЛЕДОВАТЕЛЬНОСТИ.
print('a' in 'Jack')
print('x' in 'Jack')
print(str(1) in 'Jack')

# ПРОВЕРКА СУЩЕСТВОВАНИЯ ЭЛЕМЕНТА НЕ ТОЛЬКО В СТРОКАХ, НО И В СПИСКАХ
letter_list = ['a', 'b', 'c', 'd', 1]
print('b' in letter_list)
# ПРОВЕРЯЕМ НАЛИЧИЕ ЧИСЛА Т.К. ЭТО СПИСОК
print(1 in letter_list)

# ПОЛУЧАЕМ КЛЮЧИ ПРИ ОБРАЩЕНИИ К СЛОВАРЮ
dict_1 = {1: 'a', 2: 'b', 3: 'c'}
print(5 in dict_1)
print(1 in dict_1.keys())
# ПРОВЕРКА ЗНАЧЕНИЙ, А НЕ КЛЮЧЕЙ ПРИ ПОМОЩИ МЕТОДА values
print('d' in dict_1.values())

# ФУНКЦИИ min И max
print(min(45, 90, 32, 1, 8, 9))
print(max(10, 90, 78, 104))
# НАХОЖДЕНИЕ В ЛИСТЕ МИНИМАЛЬНЫХ И МАКСИМАЛЬНЫХ ЗНАЧЕНИЙ
my_list = [1, 4, 9, 0, 3]
print(min(my_list))
print(max(my_list))

# НАХОЖДЕНИЕ МИНИМАЛЬНЫХ И МАКСИМАЛЬНЫХ ЗНАЧЕНИЙ СИМВОЛОВ СТРОКИ ПО АСКИ КОДУ
print(min('Hello!'))
print(max('Hello!'))

# ВЫВОД ПОСЛЕДОВАТЕЛЬНОСТИ АСКИ ЗНАЧЕНИЙ СИМВОЛОВ СТРОКИ
# ВЫЗОВ АСКИ ЗНАЧЕНИЙ ПРОИСХОДИТ ПРИПОМОЩИ ФУНКЦИИ ord
for letter in 'Hello!':
    print(ord(letter))
# НЕКОТОРЫЕ ФУНКЦИИ ИЗ ВСТРОЕННЫХ В PYTHON  БИБЛИОТЕК
# ПОЛУЧЕНИЕ ДОСТУПА К ФУНКЦИЯМ БИБЛИОТЕКИ ЧЕРЕЗ ЕЁ ИМПОРТ (БИБЛИОТЕКА RANDOM)
# ПЕРЕМЕШИВАНИЕ СПИСКА ПРИ ПОМОЩИ shuffle (ФУНКЦИЯ ИЗ БИБЛИОТЕКИ random)
from random import shuffle
my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)
# ВЫВОД СЛУЧАЙНОГО ЧИСЛА ПРИ ПОМОЩИ ФУНКЦИИ randint
from random import randint
print(randint(1, 100))