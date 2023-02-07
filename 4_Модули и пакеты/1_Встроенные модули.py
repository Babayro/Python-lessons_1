print('ВСТРОЕННЫЕ МОДУЛИ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
import random

x = random.randint(1, 10)
print(x)

my_list = [1, 2, 3]
random.shuffle(my_list)
print(my_list)

# МОЖНО ИМПОРТИРОВАТЬ НЕ ВЕСЬ МОДУЛЬ А КОНКРЕТНЫЙ МЕТОД
from random import randint
z = randint(1, 10)
print(z)



# МОЖЕМ ИПРОТИРОВАТЬ ФУНКЦИЮ СО СВОИМ ИМЕНЕМ
from random import shuffle as shuffle_my_list
my_list = [1, 2, 3]
shuffle_my_list(my_list)
print(my_list)

#                                               ДОМАШНЕЕ ЗАДАНИЕ

import math

print(math.sqrt(123456789))
print(math.factorial(987))
print(math.pow(876, 54))
# МОЖЕМ ИПРОТИРОВАТЬ ФУНКЦИЮ СО СВОИМ ИМЕНЕМ
from random import shuffle as shuffle_my_list
my_list = [1, 2, 3]
shuffle_my_list(my_list)
print(my_list)

#                                               ДОМАШНЕЕ ЗАДАНИЕ

import math

print(math.sqrt(123456789))
print(math.factorial(987))
print(math.pow(876, 54))
