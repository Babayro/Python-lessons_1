с = 'ООП ВВЕДЕНИЕ + АТРИБУТЫ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
# КЛАСС (АВТОМОБИЛИ) В НЁМ СОДЕРЖАТСЯ ОТРЕБУТЫ (ЦВЕТ, ГОД ВЫПУСКА)И МЕТОДЫ (ОН МОЖЕТ СИГНАЛИТЬ И БЫСТРО ЕЗДИТЬ) КОТОРЫЕ ПОТОМ СОДЕРЖАТСЯ
# В КАЖДОМ ОБЪЕКТЕ КЛАССА, ОБЪЕКТЫ (АВТОМОБИЛИ)

# ВЫЗОВ ДОКУМЕНТАЦИИ ПО КЛАССУ list
help(list)
# ПРИСВАИВАЕМ ПЕРЕМЕННОЙ СПИСОК, ПОЛУЧАЕМ ОБЪЕКТ
my_list = [1, 2, 3]
# ДАЛЕЕ С ЭТИМ ОБЪЕКТОМ МЫ МОЖЕМ РАБОТАТЬ ПРИ ПОМОЩИ МЕТОДОВ ПРЕДНАЗНАЧЕННЫХ ДЛЯ ОБЪЕКТОВ ТИПО list
my_list.append(4)
print(my_list)

# В ПАЙТОНЕ БОЛЬШОЕ КОЛИЧЕСТВО ВСТРОЕННЫХ КЛАССОВ КОТОРЫЕ ИМЕЮТ АТРИБУТЫ И МЕТОДЫ

                                     # СОЗДАЁМ СВОЙ СОБСТВЕННЫЙ КЛАСС
class MyFirstClass:
    pass
object_of_my_class = MyFirstClass()
print(type(object_of_my_class))

                                        # АТРИБУТЫ
                          # СОЗДАЕМ КЛАСС ОПИCЫВАЮЩИЙ АВТОМОБИЛЬ
# АТРИБУТ - ЭТО ФАКТИЧЕСКИ ПЕРЕМЕННАЯ КОТОРАЯ СОДЕРЖИТ ЗНАЧЕНИЯ
# МЫ ДОЛЖНЫ ЗАПИСАТЬ СПЕЦИАЛЬНЫЙ МЕТОД init =  (СОЗДАТЬ ОБЪЕКТ) ПРИ ОПРЕДЕЛЕНИИ КЛАССА (МЕТОД ЭТА ФУНКЦИЯ НАХОДЯЩАЯСЯ ВНУТРИ КЛАССА)
# ПОЭТОМУ ЗАПИСЫВАЕМ МЕТОД ПРИ ПОМОЩИ def, ПОСЛЕ ЗАПЯТОЙ В СКОБКАХ ПИШЕМ НАЗВАНИЕ АТРИБУТА КОТОРЫЙ ХОТИМ ПОМЕСТИТЬ В ЭТОТ КЛАСС
# ПРИ ПОМОЩИ КЛЮЧЕВОГО СЛОВА self ПРИСВАИВАЕМ АТРИБУТУ name ЗНАЧЕНИЕ name

class Car:
# УКАЗЫВАЕМ ОБЩИЙ АТРИБУТ КЛАССА, С ОДНИМ ПАРАМЕТРОМ ДЛЯ ВСЕХ ОБЪЕКТОВ КЛАССА
# МЫ МОЖЕМ ОБРАЩАТЬСЯ К НЕМУ НЕ ЧЕРЕЗ ОБЪЕКТ, А ЧЕРЕЗ САМ КЛАСС
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

                                  # СОЗДАЁМ ОБЪЕКТ КЛАССА Car = mazda_car
# АТРИБУТ name='ПАРАМЕТРЫ'
mazda_car = Car(name='Mazda CX 7', color='green', year='2019', is_crashed=True)
print(mazda_car.name)
print(mazda_car.color)
print(mazda_car.is_crashed)
print(mazda_car.wheels_number)

# АТРИБУТ name='ПАРАМЕТРЫ'
bmw_car =   Car(name='BMW X7', color='black', year='2021', is_crashed=False)
print(bmw_car.name)
print(bmw_car.color)
print(bmw_car.is_crashed)
print(bmw_car.wheels_number)

# К ОБЩЕМУ ПАРАМЕТРУ МЫ МОЖЕМ ОБРАЩАТЬСЯ НЕ ЧЕРЕЗ ОБЪЕКТ, А ЧЕРЕЗ САМ КЛАСС
number_of_wheels_of_3_cars = Car.wheels_number * 3
print(number_of_wheels_of_3_cars)
                                               # Домашнее задание
class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes

post_for_cocs = BlogPost('Jack', 'I love grill!', 76)
post_for_driver = BlogPost('Sipa', 'I\'am a good driver!', 100)

post_for_cocs.number_of_likes = 1500

print(post_for_cocs.number_of_likes)
print(post_for_driver.number_of_likes)