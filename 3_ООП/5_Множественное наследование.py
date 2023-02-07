fhjgujyu = 'МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'

class Swimable:
    def __init__(self, name):
        print('Method init() of Swimable')
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and i can swim')

    def swim(self):
        print('i\'m swiming')

class Walkable:
    def __init__(self, name):
        print('Method init() of Walkable')
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and i can walk')

    def walk(self):
        print('i\'m walking')


class Flyable:
    def __init__(self, name):
        print('Method init() of Flyable')
        self.name = name

    def greeting(self):
        print(f'Hello! My name is {self.name} and i can fly')

    def fly(self):
        print('i\'m flying')

# greeting ВЫВОДИТСЯ В ПОРЯДКЕ УКАЗАННОМ НИЖЕ В СКОБКАХ
class GameCharacter(Walkable, Swimable, Flyable):
    def __init__(self, name):
        print('Method init() of GameCharacter')
        self.name = name
 # ВЫВОДЯТСЯ В УКАЗАННОМ НИЖЕ ПОРЯДКЕ
        Flyable.__init__(self, name)
        Walkable.__init__(self, name)
        Swimable.__init__(self, name)
    # def greeting(self):
    #     print(f'Hello! My name is {self.name}')


james = GameCharacter('James')
james.greeting()
james.swim()
james.walk()
james.fly()
print(isinstance(james, Walkable))
print(isinstance(james, object))
print(isinstance(james, dict))