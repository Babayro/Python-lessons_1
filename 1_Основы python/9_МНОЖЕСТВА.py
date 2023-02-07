# 6). МНОЖЕСВА (SETS)
множества = 'МНОЖЕСТВА (SETS) РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(множества)
# МНОЖЕСТВА ЭТО НЕУПОРЯДОЧЕННАЯ КОЛЛЕКЦИЯ УНИКАЛЬНЫХ ЭЛЕМЕНТОВ
# В МНОЖЕСТВЕ НЕ МОЖЕТ БЫТЬ ДВУХ ОДИНАКОВЫХ ОБЪЕКТОВ
# МНОЖЕСТВО sets ОТМЕЧАЕТСЯ С ПОМОЩЬЮ {} ТАКЖЕ КАК И dictionary (словари)
# НО В ОТЛИЧИЕ ОТ СЛОВАРЕЙ СЮДА ПОМЕЩАЕТСЯ НЕ ПАРА КЛЮЧ И ЗНАЧЕНИЕ, А ПРОСТО ЗНАЧЕНИЕ
rainbow_colors = {'red', 'orange', 'green', 'blue', 'indigo', 'violet'}
print(rainbow_colors)
# ФУНКЦИЯ ОПРЕДЕЛЕНИЯ ТИПА ПЕРЕМЕННОЙ
print(type(rainbow_colors))
# СОЗДАНИЕ ПУСТОГО МНОЖЕСТВА ПРИ ПОМОЩИ ФУНКЦИИ set
empty_set = set()
print(type(empty_set))
# МЫ МОЖЕМ СОЗДАВАТЬ МНОЖЕСТВА ИЗ СПИСКОВ И КОРТЕЖЕЙ
number_list = [1, 2, 3, 4, 5]
tuple_1 = ('hello', 'up', 'down')
set_from_list = number_list
set_from_tuple = tuple_1
print(set_from_list)
print(set_from_tuple)
# ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ В set ПРИ ПОМОЩИ МЕТОДА append и add(ДОБАВТЬ)
set_from_list.append(777)
print(set_from_list)

# УДАЛЕНИЕ СЛУЧАЙНОГО ЭЛЕМЕНТА ИЗ МНОЖЕСТВА ПРИ ПОМОЩИ МЕТОДА pop
set_from_list.pop()
print(set_from_list)
# УДАЛЕНИЕ ВЫБРАННОГО ЭЛЕМЕНТА ПО НАЗВАНИЮ ПРИ ПОМОЩИ МЕТОДА remove
set_from_list.remove(1)
print(set_from_list)
# УДАЛЕНИЕ ЭДЕМЕНТА ПРИ ПОМОЩИ МЕТОДА discard
# ОЧИСТКА МНОЖЕСТВА
set_from_list.clear()
print(set_from_list)

#ДОМАШНЕЕ ЗАДАНИЕ
text_set = set('Создайте множество при помощи функции set() '
                  'из текста, чтобы получить уникальные символы, '
                  'содержащиеся в тексте.')
print(text_set)