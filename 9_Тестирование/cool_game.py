# TDD СНАЧАЛО ПИШЕМ ТЕСТЫ, А ПОТОМ СОЗДАЁМ НУЖНЫЕ НАМ ФУНКЦИИ ИЛИ КЛАССЫ
# ФУНКЦИЯ ПРИВЕТСВИЯ ПЕРСОНАЖА
from random import choice

def greet(name, isEnemy):
    if isEnemy:
        return f'Hello {name}! I will kill you, bastard!'
    else:
        return f'Hello {name}! How are you?'


#   ФУНКЦИЯ ПОЕДАНИЯ ГАМБУРГЕРОВ

def eat_burgers(number):
    if number > 3:
        return 'Oh! I overate!'
    else:
        return 'Mmm! That was exellent!'

def can_fly(name):
    if name == 'Batman':
        return True
    else:
        return False
# ФУНКЦИЯ АРСЕНАЛ ОРУЖИЯ

def get_arsenal():
    return choice(('knife', 'handgun', 'machine gun'))# choice СЛУЧАЙНЫМ ОБРАЗОМ НАХОДИТ ОРУЖИЕ
