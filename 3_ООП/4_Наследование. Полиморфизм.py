rtth = 'НАСЛЕДОВАНИЕ, ПОЛИМОРФИЗМ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
# INHERENTANCE (НАСЛЕДОВАНИЕ)
class Car:
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('Car is created')

    def driver(self, city):
        print(self.name + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color
        print('Coloro is change to ' + new_color)

class Truck(Car):
# ПЕРЕОПРЕДЕЛЯЕМ АТРИБУТ В ОБЪЕКТЕ КЛАССА
    wheels_number = 6

    def __init__(self, name, color, year, is_crashed):
      Car.__init__(self, name, color, year, is_crashed)
      print('Truck is created')
# ПЕРЕОПРЕДЕЛЯЕМ ПАРАМЕТРЫ МЕТОДА driver
    def driver(self, city):
        print('Truck ' + self.name + ' is driving to ' + city)
    def load_cargo(self, weight):
     print('The cargo is loaded. Weight is ' + str(weight))
#ПОСЛЕ ОПРЕДЕЛЕНИЯ КЛАССА НАДО ОТСТУПАТЬ ДВЕ СТРОЧКИ ПЕРЕД ОПРЕДЕЛЕНИЕМ ОБЪЕКТА КЛАССА

man_truck = Truck('MAN', 'Blue', '2005', False)

man_truck.driver('Riga')
print(man_truck.wheels_number)

print (man_truck.color)

man_truck.change_color('white')
print(man_truck.color)

man_truck.load_cargo(2000)

                # ПОЛИМОРФИЗМ


class Animals:
    def __init__(self, name):
        self. name = name
    def speak(self):
        raise NotImplementedError('Class successor must implement this method')

class Dog(Animals):
    def __init__(self, name):
        self. name = name

    def speak(self):
        print(self.name + ' is saving wow')


class Cat(Animals):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saving meow')

class Maus(Animals):
    def __init__(self, name):
        self. name = name

    def speak(self):
        print(self.name + ' peeee-peeee')

class Fish(Animals):
    def __init__(self, name):
        self. name = name

    def speak(self):
        print(self.name + ' is saving nothing')


spike = Dog('Spike')
tom = Cat('Tom')
jery = Maus('Jery')
freddy = Fish('Freddy')
pet_list = [spike, tom, jery, freddy]

for pet in pet_list:
    pet.speak()

def pet_voice(pet):
    pet.speak()
pet_voice(tom)
pet_voice(spike)
pet_voice(freddy)

                                    # ДОМАШНЕЕ ЗАДАНИЕ.
class GameCharahter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self. level = level
    def speak(self):
        print('Hi, my name is ' + self.name)


class Villain(GameCharahter):
    def __init__(self, name, health, level):
        GameCharahter.__init__(self, name, health, level)
    def speak(self):
        print('Hi, my name is ' + self.name + ' I will kill you!')

    def kill(self, assign):
        assign.health = 0
        print('Bang-bang, now you\'re dead')


sony = GameCharahter('Sony', 30, 80)
slon = Villain('Slon', 40, 150)

sony.speak()
slon.speak()
print(sony.health)
slon.kill(sony)
print(sony.health)
