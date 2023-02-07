popofo = 'МЕТОДЫ КЛАССА, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
#self - ЭТО МЕТОД УОВНЯ ОБЪЕКТА, cls - ЭТО МЕТОД УРОВНЯ КЛАССА
class Gamer:

    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers
# СОЗДАЁМ ОБЪЕКТ КЛАССА ПРИ МОМОЩИ МЕТОДА КЛАССА
    @classmethod
    def gamer_from(cls):
        john = cls('jony 777', 19, 78, 1500)
        print(john.get_age())
# СОЗДАЁМ ОБЪЕКТ КЛАССА ИЗ ТЕКСТОВОГО ФАЙЛА ПРИ МОМОЩИ МЕТОДА cls
    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, level, points = data_string.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1
    def log_out(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level
    def get_points(self):
        return self.points
    def is_adult(self):
        return self.age >= 18
    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can go to adult level ')
        else:
            print('You can\'t go to adult level')
print(Gamer.active_gamers)

gamer_1 = Gamer('Pidor', 21, 150, 1500)

print(Gamer.active_gamers)

gamer_2 = Gamer('Sips', 14, 50, 550)

print(Gamer.active_gamers)

gamer_1.get_adult_level_permission()
gamer_2.get_adult_level_permission()

gamer_1.log_out()
print(Gamer.active_gamers)
print(Gamer.get_active_gamers())
Gamer.gamer_from()

james = Gamer.gamer_from_string('James, 18, 150, 1500')
print(james.get_age())
# ВСТРОЕННЫЙ КЛАСС СЛОВАРЬ КОТОРЫЙ МОЖЕТ СОЗДАВАТЬ СЛОВАРИ ИЗ СПИСКОВ

my_dict = dict.fromkeys((1, 2, 3), ('apple', 'orange', 'banana'))
print(my_dict)