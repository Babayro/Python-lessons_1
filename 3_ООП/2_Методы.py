met = 'МЕТОДЫ, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'

#МЕТОД - ЭТО ФУНКЦИЯ КОТОРАЯ ВЫПОЛНЯЕТ КАКИЕ-ТО ДЕЙСТВИЯ
class Car:
# УКАЗЫВАЕМ ОБЩИЙ АТРИБУТ КЛАССА, С ОДНИМ ПАРАМЕТРОМ ДЛЯ ВСЕХ ОБЪЕКТОВ КЛАССА
# МЫ МОЖЕМ ОБРАЩАТЬСЯ К НЕМУ НЕ ЧЕРЕЗ ОБЪЕКТ, А ЧЕРЕЗ САМ КЛАСС
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
# СОЗДАЁМ МЕТОД КЛАССА, МОЖЕМ КОНКАТЕНИРОВАТЬ С ЛЮБЫМ АТРИБУТОМ КЛАССА,  МОЖЕМ ДОБАВИТЬ ПОЗИЦИОННЫЙ АРГУМЕНТ
    def drive(self, city):
        print(self.name + ' Car is driving' + city)
# МОЖЕМ СОЗДАТЬ МЕТОД КОТОРЫЙ БУДЕТ МЕНЯТЬ ЗНАЧЕНИЯ АТРИБУТОВ, ЧЕРЕЗ self МЫ ОБРАЩАЕМСЯ К АТРИБУТУ
    def chaenge_color(self, new_color):
        self.color = new_color

# СОЗДАЁМ ОБЪЕКТ  КЛАССА
opel_car = Car('Opel Tigra', 'grey', '1999', True)
# ОБРАЩАЕМСЯ К МЕТОДУ КЛАССА
opel_car.drive(' London')
mazda_car = Car('Mazda CX7', 'Blacx', '2007', False)
mazda_car.drive(' Parish')
mazda_car.chaenge_color('yellow')
print(mazda_car.color)
print(opel_car.name)
print(opel_car.wheels_number)
print(opel_car.color)
print(opel_car.year)
print(opel_car.is_crashed)

class Circle:
# ОБЩИЙ АТРИБУТ КЛАССА, С ОДНИМ ПАРАМЕТРОМ ДЛЯ ВСЕХ ОБЪЕКТОВ КЛАССА
    pi = 3.14
# СОЗДАЁМ АТРУБУТ
    def __init__(self, radius=1):
        self.radius = radius
# СОЗДАЁМ МЕТОД ВОЗВРАЩАЮЩИЙ РАДИУС ОКРУЖНОСТИ
    def get_area(self):
        return self.pi * (self.radius ** 2)
# СОЗДАЁМ МЕТОД ВОЗВРАЩАЮЩИЙ ДЛИНУ ОКРУЖНОСТИ
    def get_circumference(self):
        return 2 * self.pi * self.radius

#СОЗДАЁМ ОБЪЕКТ КЛАССА
circl_1 = Circle(3)
print(circl_1.get_area())
circl_2 = Circle(5)
print(circl_2.get_area())
circl_3 = Circle()
print(circl_3.get_circumference())
                                         # ДОМАШНЕЕ ЗАДАНИЕ
class BankAccount:

    def __init__(self, client_id, client_first_name, client_last_name):
        self.clietn_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = 0.0
    def add (self, summ):
        self.balance += summ

    def with_draw (self, summ):
        self.balance -= summ
accoun_1 = BankAccount(1, 'Ken', 'Hrenov')
accoun_2 = BankAccount(2, 'Hren', 'Kenov')

accoun_1.add(100)
print(accoun_1.balance)

accoun_2.with_draw(50)
print(accoun_2.balance)