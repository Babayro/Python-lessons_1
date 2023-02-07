ergegk = 'СПЕЦИАЛЬНЫЕ МАГИЧЕСКИЕ МЕТОДЫ, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
# СПЕЦИАЛЬНЫЕ МЕТОДЫ НАЧИНАЮТСЯ ДВУМЯ ЗНАКАМИ ПОДЧЁРКИВАНИЕ И ЗАКАНЧИВАЮТСЯ ИМИ


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
#СОЗДАЁМ МЕТОД ДЛЯ РАСПЕЧАТКИ ИМЕНИ И ФАМИЛИИ, ЕСЛИ БЕЗ МЕТОДА ПРОСТО РАСПЕЧАТАЕТСЯ ОБЪЕКТ С НОМЕРОМ В ПАМЯТИ
    def __str__(self):
        return self.first_name + ' ' + self.last_name
# СОЗДАЁМ МЕТОД ДЛЯ ВЫВОДА ВОЗРАСТА
    def __len__(self):
        return self.age
    def __add__(self, other):
        return self.age + other.age
 # УДАЛЯЕМ ССЫЛКУ НА ОБЪЕКТ В ПАМЯТИ
    def __del__(self):
        print('Person object with name ' + self.first_name + ' is deleted from memory')

jack = Person('jack', 'White', 45)
clizma = Person('Clizma', 'Huizma', 20)

print(jack + clizma)

print(len([1, 2, 3, 4, 5]))
print(jack)
print(len(jack))
del(jack)
x = 5 + 5
y = '5' + '5'
print(x, y)
print(type(x), type(y))
x = 5
y = 3

a = '5'
b = '3'

print(x + y)
print(a + b)

print(x.__add__(y))
print(a.__add__(b))

#                                           ДОМАШНЕЕ ЗАДАНИЕ

class Chain():
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return "Chain with " + str(self.number_of_items)

    def __len__(self):
        return self.number_of_items


chain_1 = Chain(23)
chain_2 = Chain(32)

print(chain_1)
print(chain_2)

print(len(chain_1))
print(len(chain_2))