rgth = 'МОДУЛЬ shelve (ПОЛКА, ХРАНИТЬ НА ПОЛКЕ), РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(rgth)

# ДАННЫЙ МОДУЛЬ ЭТО АЛЬТЕРНАТИВА МОДУЛЮ pickle. ОН ИСПОЛЬЗУЕТСЯ КОГДА НУЖНО СОХРАНИТЬ МНОГО ОБЪКТОВ ИЛИ БОЛЬШИЕ ОБЪЕКТЫ
# И ЧТОБЫ НЕ НАГРУЖАТЬ ПАМЯТЬ КОМПЬЮТЕРА ОН СОХРАЯЕТ ЭТИ ОБЪЕКТЫ НЕ В ПАМЯТИ, А ФАИЛОВОЙ СИСТЕМЕ ВВИДЕ ПАР КЛЮЧ И ЗНАЧЕНИЕ (КАК В СЛОВАРЕ)
# ДАННЫЙ МЕТОД ИСПОЛЬЗУЕТ ТЕЖЕ МЕТОДЫ, ЧТО И СЛОВАРЬ
# ЗНАЧЕНИЯ МАРИНУЮТСЯ, СОХРАНЯЮТСЯ ТАКЖЕ КАК КОГДА ИСПОЛЬЗУЕТСЯ МОДУЛЬ pickle

import shelve

with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'

    print(cars['ford'])
    print(cars['renault'])
    print(cars['opel'])

    for keys in cars:
        print(keys)

# ЕСЛИ ОПЕЧАТАТЬСЯ ОН СОХРАНИТ В ФАИЛЕ НОВОЕ ЗНАЧЕНИЕ С ОПЕЧАТКОЙ В СТАРЫХ ВЕРСИЯХ PYTHON 3
# print(cars['ope']) ЧТОБЫ УДАЛИТЬ НЕВЕРНОЕ ЗНАЧЕНИЕ del cars['ope']

# ЕСЛИ ЗА ПРЕДЕЛАМИ БЛОКА МЫ ОБРАТИМСЯ К ОБЪЕКТУ cars ТО БУДЕТ ОШИБКА
#print(cars['mazda']) КОГДА МЫ ИСПОЛЬЗУЕМ with БЛОК, ТО ФАЙЛ АВТОМАТИЧЕСКИ ЗАКРЫВАЕТСЯ КОГДА МЫ ВЫХОДИМ ЗА ЕГО ПРИДЕЛЫ
# Т.Е. КОГДА МЫ НАЧИНАЕМ ПИСАТЬ КОД С НОВОЙ СТРОКИ БЕЗ ОТСТУПА
# ТАКЖЕ В ОКНЕ ПРОЕКТА У НАС СОЗДАЁТСЯ ФАЙЛ shelve_test, МЫ НЕ МОЖЕМ ОТКРЫТЬ ЕГО В ТЕКСТОВОМ РЕЖИМЕ Т.К. ЭТОТ ФАИЛ ЕСТЬ БАЗА ДАННЫХ В КОТОРОМ СОЗДАЁТСЯ ОБЪЕКТ
# ЕСЛИ МЫ ПРОСТО СОЗДАДИМ СЛОВАРЬ ТО ОН СОЗДАЁТСЯ В ПАМЯТИ, А ДАННЫЙ ОБЪЕКТ СОЗДАЁТСЯ В БАЗЕ ДАННЫХ

                                     #РАБОТА С ДАННЫМИ ПРИ ПОМОЩИ МОДУЛЯ shelve
# ВЫВОДИМ ВСЕ КЛЮЧИ И ЗНАЧЕНИЯ
    cars['kia'] = 'South Korea'
    for key in cars:
        print(key + ': ' + cars[key])
# ВВОДИМ КЛЮЧ МОДЕЛЬ МАШИНЫ И ВЫВОДИМ ЗНАЧЕНИЕ СТРАНА МАШИНЫ
    while True:
        key = input('Please enter a car name: ')
        if key == 'quit':
            break
        country = cars.get(key, "We don't have a " + key)
        print(country)
# ЕСЛИ В ОКНЕ ВВОДА НАБРАТЬ quit ТО МЫ ВЫДИМ ИЗ ЦИКЛА, ИНАЧЕ БУДЕТ БЕСКОНЕЧНО ВЫВОДИТЬСЯ ОКНО ВВОДА

    while True:
        key = input('Please enter a car name: ')
        if key == 'quit':
            break
        if key in cars:
            county = cars[key]
            print(country)
        else:
            print("We don't have a " + key)

# ВЫВОДИМ ВСЕ КЛЮЧИ И ЗНАЧЕНИЯ
    for key in cars:
            print(key + ' ' + cars[key])
    print('СОРТИРУЕМ ПО АЛФАВИТУ')
# РАСПОЛОГАЕМ ВСЕ КЛЮЧИ В АЛФАВИТНОМ ПОРЯДКЕ
    ordered_keys_list = list(cars.keys())
    ordered_keys_list.sort()

    for key in ordered_keys_list:
        print(key + ' ' + cars[key])

# РАСПЕЧАТЫВАЕМ ТОЛЬКО ЗНАЧЕНИЯ
    for value in cars.values():
        print(value)
    print(cars.values())
# РАСПЕЧАТЫВАЕМ ТОЛЬКО КЛЮЧИ
    for key in cars.keys():
        print(key)
    print(cars.keys)
# РАСПЕЧАТЫВАЕМ КОРТЕЖИ С КЛЮЧОМ И ЗНАЧЕНИЕМ
    for item in cars.items():
        print(item)
    print(cars.items())
# СОЗДАЕМ ЕЩЁ ОДИН ФАЙЛ shelve И ОБЪЕКТ, В ТАКОЙ ФОРМЕ ЗАПИСИ МЫ МОЖЕМ ОБРАТИТЬСЯ К САМОМУ ОБЪЕКТУ cars И К ПРИМЕРУ ОПРЕДЕЛИТЬ САМ ОБЪЕКТ И ЕГО КЛАСС
# В ТАКОЙ ФОРМЕ ЗАПИСИ НЕТ ОТСТУПОВ, НО ОБЯЗАТЕЛЬНО ЗАКРЫТЬ ОБЪЕКТ ПРИ МОМОЩИ МЕТОДА close
cars = shelve.open('shelve-test1')

cars['opel'] = 'Germany'
cars['ford'] = 'USA'
cars ['mazda'] = 'Japan'
cars ['renault'] = 'France'

print(cars['ford'])
print(cars['renault'])
# РАСПЕЧАТЫВАЕМ ОБЪЕКТ
print(cars)
# РАСПЕЧАТЫВАЕМ КЛАСС ОБЪЕКТА
print(type(cars))
# ЗАКРЫВАЕМ ОБЪЕКТ-
cars.close()