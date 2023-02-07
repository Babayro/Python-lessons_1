цикл_фор = 'ЦИКЛ for РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(цикл_фор)
# ЦИКЛ for НУЖЕН ДЛЯ ПЕРЕБОРА ПОСЛЕДОВАТЕЛЬНОСТИ ЭЛЕМЕНТОВ И ОПЕРАЦИЙ НАД НИМИ
# МОЖНО ПЕРЕБИРАТЬ СТРОКИ,СПИСКИ, СЛОВАРИ, МНОЖЕСТВА И Т.Д.
# ДЛЯ ПЕРЕМЕННОЙ number ИЗ ЧИСЕЛ В ПЕРЕМЕННОЙ number_list МЫ БУДЕМ ПРОИЗВОДИТЬ КАКИЕ ТО ДЕЙСТВИЯ,ВЫВОДИТЬ ЧИСЛА
# number НЕ СПИСОК, А ПРОСТО ПЕРЕМЕННАЯ, ПОЭТОМУ ЧИСЛА ВЫВОДЯТЬСЯ ВЕРТИКАЛЬНО.
# ЦИКЛ for ПЕРЕБИРАЕТ И ВЫВОДИТ Т.Е. ПРОИЗВОДИТ УКАЗАННОЕ ДЕЙСТВИЯ СО ВСЕМИ ЭЛЕМЕНТАМИ СПИСКА
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print(number)

# ВЫВЕДЕТ "Hi" СТОЛЬКО РАЗ, СКОЛЬКО ЭЛЕМЕНТОВ В СПИСКЕ
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print('Hi')
    print('Ola!')

# ЭЕМЕНТЫ СПИСКА ПРИОБРАЗУЕМ В СТРОКИ ПРИ ПОМОЩИ КОМАНДЫ str И КОНКАТЕНИРУЕМ ССО СТРОКОЙ Hola
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print(str(number) + '. Hola')
# ПРОВЕРЯЕМ ЧИСЛА СПИСКА НА ЧЁТНОСТЬ, ЕСЛИ True ТО ВЫВОДИМ В НОВУЮ ПЕРЕМЕННУЮ
# print НУЖНО СДВИГАТЬ В ПРАВО НА 1 ПРОБЕЛ ИЗ ПОД УСЛОВИЯ ЕСЛИ PUCHARM ПОДСКАЗЫВАЕТ КРАСНЫМ!!!
# ЕСЛИ НАЧИНАЕМ БЕЗ ОТСТУПА С НОВОЙ СТРОКИ ТО ЭТА КОМАНДА БУДЕТ ЗА ЦИКЛОМ, ПОЭТОМУ НУЖЕН ОТСТУП!!!
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    if number % 2 == 0:
     print(number)
    else:
        print('Hey!')
# ВЫЧЕСЛЯЕМ СУММУ ЧИСЕЛ СПИСКА
# СКЛАДЫВАЕТ ПЕРВЫЕ 2 ЧИСЛО, ЗАТЕМ ИХ СУММУ ПРИБАВЛЯЕТ К ТРЕТЬЕМУ (СЛЕДУЮЩЕМУ ЧИСЛУ)
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summ_numer_list = 0
for number in number_list:
    summ_numer_list = summ_numer_list + number
    print(summ_numer_list)

# ЕСЛИ print ВЫВЕСТИ С НОВОЙ СТРОКИ БЕЗ ОТСТУПА ТО МЫ ПОЛУЧИМ СРАЗУ ОКОНЧАТЕЛЬНЫЙ РЕЗУЛЬТАТ
# БЕЗ ПЕРЕБОРА ВСЕХ ВАРИАНТОВ ДО ОКОНЧАТЕЛЬНОГО, ПОТОМУ ЧТО КОМАНДА НА ВЫПОЛНЕНИЕ ДЕЙСТВИЯ
# ВНОВОЙ СТРОКЕ БЕЗ ОТСТУПА БУДЕТ ОЗНАЧАТЬ
# ВЫХОД ИЗ ЦИКЛА!!! ЗА ОТСТУПАМИ НУЖНО ВНИМАТЕЛЬНО СЛЕДИТЬ!!!
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summ_numer_list = 0
for number in number_list:
    summ_numer_list = summ_numer_list + number
print(summ_numer_list)

# ПЕРЕБОР СТРОК.!!!for В КАКУЮ ПЕРЕМЕННУЮ КЛАДЁМ РЕЗУЛЬТАТ in В КАКОЙ ПЕРЕМЕННОЙ БУДУТ ПРОИСХОДИТЬ МАНИПУЛЯЦИИ!!!
greeting = 'Hello Python'
for letter in greeting:
    print(letter)


# ВЫВОД КОНКРЕТНЫХ СИМВОЛОВ
greeting = 'Hello Python'
for letter in greeting:
    if letter == 'l':
     print(letter)
# ВЫВОД БЕЗ БУКВЫ LL
greeting = 'Hello Python'
for letter in greeting:
    if letter != 'l':
     print(letter)

# ЗАПУСК ЦИКЛА БЕЗ ПЕРЕМЕННОЙ, А ПРОСТО С САМОЙ СТРОКИ
for letter in 'Hello Python':
    if letter != 'o':
     print(letter)

# ВЫВОДИМ ТЕКСТ СТОЛЬКО РАЗ, СКОЛЬКО БУКВ В СТРОКЕ
for letter in 'Hello Python':
     print('I\'m a python developer')

# СПИСОК В КОТОРОМ НАХОДЯТСЯ ОБЪЕКТЫ tuple Т.Е. ЛИСТ С НЕСКОЛЬКИМИ КАРТЕЖАМИ.
tupple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for item in tupple_list:
    print(item)
# РАСПАКОВКА ОБЪЕКТА tupple В ЦИКЛЕ
for letter_1, letter_2, in tupple_list:
    print(letter_1, letter_2,)
# ВЫВОД КАЖДОГО СИМВОЛА С НОВОЙ СТРОКИ
for letter_1, letter_2, in tupple_list:
    print(letter_1)
    print(letter_2)
# ВЫВЕДУТСЯ ТОЛЬКО КЛЮЧИ!!!
dictionarie = {'key 1': 'value 1', 'key 2': 'value 2', 'key 3': 'value 3', 'key 4': 'value 4'}
for item in dictionarie:
    print(item)
# ЧТОБЫ ОБРАТИТЬСЯ И К КЛЮЧАМ И ЗНАЧЕНИЯМ ИСПОЛЬУЕМ МЕТОД items
dictionarie = {'key 1': 'value 1', 'key 2': 'value 2', 'key 3': 'value 3', 'key 4': 'value 4'}
for item in dictionarie.items():
    print(item)
# ДЛЯ ВЫЗОВА КЛЮЧЕЙ ИСПОЛЬЗУЕМ МЕТОД keys
for item in dictionarie.keys():
    print(item)
# ДЛЯ ВЫЗОВА ЗНАЧЕНИЙ ИСПОЛЬЗУЕМ МЕТОД values
for item in dictionarie.values():
    print(item)
# ВЫВОД БЕЗ МЕТОДОВ ЧЕРЕЗ print
for item in dictionarie:
    print('key', 'value')
for item in dictionarie:
    print('key')

newmethod = 'RESUIT'
print('RESUIT')
# РАСПАКОВКА КЛЮЧЕЙ
for value in dictionarie:
    print(value)
# РАСПАКОВКА ЗНАЧЕНИЙ ПРИ ПОМОЩИ items И value
for key,value in dictionarie.items():
    print(value)
# РАСПАКОВКА КОЛЮЧЕЙ
for key in dictionarie:
    print(key)
# ЕСЛИ МЫ ХОТИМ СДЕЛАТЬ КАКОЕТО ДЕЙСТВИЕ, НО НЕ ХОТИМ ПРИВЗЫВАТЬСЯ НИ К СТРОКЕ НЕ СПИСКУ И Т.Д.
# ЭТО МОЖНО СДЕЛАТЬ ПРИ ПОМОЩИ ФУНКЦИИ range
for x in range(5):
    print(x)
# ВЫВОД ПРИ ПОМОЩИ _ - ЭТО ПЕРЕМЕННАЯ ИСПОЛЬЗУЕТСЯ КОГДА САМА ПЕРЕМЕННАЯ НЕ ВАЖНА, А ИСПОЛЬЗУТСЯ ДЛЯ ИТЕРАЦИИ
for _ in range(5):
    print('Hello')


# ДОМАШНЕЕ ЗАДАНИЕ

# ЗАДАЧА 1
number_sum = 0
for number in range(10, 31):
    if number % 2 == 0:
        number_sum += number
        print(number_sum)

# ЗАДАЧА 2
number = input('Please, enter any in integer number')
for _ in range(int(number)):
    print('Hello!!!')