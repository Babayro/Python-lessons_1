print('ТИПЫ ОШИБОК, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')

# ОПЕЧАТКА
# SyntaxError
# des function_1():
#     x = 1+ 1
#     print(x)

# НЕ ОПРЕДЕЛИЛИ ПЕРЕМЕННУЮ Т.К. НЕТ ОТСТУПА, ВЫШЛИ ЗА БЛОК КОДА
# NameError
# print(x)

# НЕТ ДЛИНЫ СПИСКА
# TypeError
# len(1)
# my_list = [1, 2, 3]
# print(my_list + 'hello')

# ОШИБКА Т.К. СЧЁТ В СПИСКЕ НАЧИНАЕТСЯ С 0
# IndexError
# my_list = [1, 2, 3]
# print(my_list[3])

# ОШИБКА ИНТЕДЖЕР И СТРОКА
# ValueError
# print(int('43'))
# print(int('he'))

# ОШИБКА: НЕТ ТАКОГО КЛЮЧА В СЛОВАРЕ
# KeyError
# my_dict = {'first':'apple', 'second':'orange'}
# my_dict['third']
#
# ОШИБКА: У СТРОК НЕТ ТАКОГО АТРИБУТА
# AttributeError
# 'red'.attr()