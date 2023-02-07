function = 'СОЗДАНИЕ ФУНКЦИЙ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
# BUILT-IN FUNCTIONS (ВСТРОЕННЫЕ ФУНКЦИИ)
x = print('Hello!!!') # НИЧЕГО НЕ ВОЗВРАЩАЕТ, А ПРОСТО РАСПЕЧАТЫВАЕТ, СЛОВО В КАВЫЧКАХ ЭТО АРГУМЕНТ!!!
y = set() # СОЗДАЁТ ПУСТОЕ МНОЖЕСТВО
print(type(x)) # ПРОВЕРЯЕМ ТИП ФУНКЦИИ (НИЧЕГО НЕ ВОЗВРАЩАЕТ)
print(type(y)) # ВОЗВРАЩЫЕТ ПУСТОЕ МНОЖЕСТВО


# BUILT-IN METHODS (ВСТРОЕННЫЕ МЕТОДЫ) МЕТОДЫ ЭТО ФАКТИЧЕСКИ ТЕЖЕ ФУНКЦИИ
my_list = [1, 2, 3]
my_list.append(4) # append ЭТО МЕТОД ВОЗВРАЩАЮЩИЙ ПАРАМЕТРЫ, 4-ЭТО АРГУМЕНТ
print(my_list)
my_list.clear() # МЕТОД БЕЗ ПАРАМЕТРОВ, Т.Е. НИЧЕГО НЕ ВОЗВРАЩАЕТ
print(my_list)
                                          # СОЗДАНИЕ ФУНКЦИЙ (CREATING FUNCTIONS)
def print_greeting(): # def = ОПРЕДЕЛЯЕМ ФУНКЦИЮ, ИМЯ ФУНКЦИИ, () = ОБОЗНАЧАЕМ ЧТО ЭТО ФУНКЦИЯ
 # ДОКУМЕНТАЦИЯ ОПИСЫВАЮЩАЯ ЧТО ДЕЛАЕТ ФУНКЦИЯ И, ЧТО ВОЗВРАЩАЕТ
    '''
     print 'Hello!!!' text
    :return: None
    '''
    print('Hello!!!')
print_greeting() # ВЫЗЫВАЕМ ФУНКЦИЮ CALL THE FUNCTION
help(print_greeting) # ПРОСМОТР ДОКУМЕТНАЦИИ ФУНКЦИИ

                        # ФУНКЦИЯ С ДОПОЛНИТЕЛЬНЫМ ПАРАМЕТРОМ
def print_greeting_with_name(name):
    '''
    :param name
    :return: None
    '''
    print('Hello' + ' ' + name + ' ' + '!') # ТЕЛО ФУНКЦИИ
print_greeting_with_name('Sipa') # ПРИСВАИВАЕМ ЗНАЧЕНИЕ

def print_greeting_with_name(name = 'Jam'): # ПРИСВАИВАЕМ ЗНАЧЕНИЕ
    '''
    :param name
    :return: None
    '''
    print('Hello' + ' ' + name + ' ' + '!')
print_greeting_with_name()
help(print_greeting_with_name) # ПРОСМОТР ДОКУМЕНТАЦИИ ФУНКЦИИ

                            # СОЗДАЁМ ФУНКЦИЮ КОТОРАЯ ВОЗВРАЩАЕТ РЕЗУЛЬТАТ, Т.Е. ВОЗВРАЩАТЬ РЕЗУЛЬТАТ ДЕЙСТВИЙ В НОВУЮ ПЕРЕМЕННУЮ
# ФУНКЦИЯ ПРОВЕРКИ НАЛИЧИЯ ТЕКСТА
def is_hellou_in_text(text):
    if 'hellou' in text.lower(): # ПРОИЗВОДИМ ОПЕРАЦИЮ С ПАРАМЕТРОМ, ТЕКСТОМ
        return True
    else:
        return False
print(is_hellou_in_text('Hellou everyone'))

# ТОЖЕ САМОЕ ТОЛЬКО В УПРАЩЁННОЙ ФОРМЕ
def is_hellou_in_text(text):
    return 'hellou' in text.lower() # ПРОИЗВОДИМ ОПЕРАЦИЮ С ПАРАМЕТРОМ, ТЕКСТОМ
print(is_hellou_in_text('Hellou everyone'))

# ПОИСК СТРОКИ В ТЕКСТЕ
def string_in_text(string, text):
    return string in text
print(string_in_text('he', 'the apple'))
print(string_in_text('hey', 'the apple'))

# ФУНКЦИЯ КОТОРАЯ БУДЕТ СОВЕРШАТЬ ДЕЙСТВИЕ И ВОЗВРАЩАТЬ РЕЗУЛЬТАТ
# ВЫЖНО!!! return ПИШЕМ ПОСЛЕ ТЕЛА КОДА ИСПОЛНЕНИЯ, ПОСЛЕ return ПРОИСХОДИТ ВЫХОД ИЗ ФУНКЦИИ
def greeting_depends_of_gender(name, gender):
    if gender == 'male':  # ТЕЛО ФУНКЦИИ
        print('Hello! ' + name + ' You are look good!')
        return gender
    elif gender == 'female':
        print('Hello ' + name + "You are so nice!")
        return gender
    else:
        print('Hello! ' + name + 'I dont know you are!')
        return gender

return_value_1 = greeting_depends_of_gender('Jack ', 'male') # ВЫЗОВ ФУНКЦИИ
return_value_2 = greeting_depends_of_gender('Jane ', 'female')
return_value_3 = greeting_depends_of_gender('Ja ', 'cemale')

print(return_value_1)
print(return_value_2)
print(return_value_3)

# ДОМАШНЕЕ ЗАДАНИЕ

def cat_voice():
   print('Meow!')
cat_voice()

def dog_voice():
    print('Woof!!!')
dog_voice()

def cat_voce_1():
    return 'Meow!!!'

def dog_voce_1():
    return 'WOOF!!!'
print(cat_voce_1())
print(cat_voce_1())
print(dog_voce_1())
print(dog_voce_1())

def get_voice():
    return str() + '!'
print(get_voice())



def get_odd_number_list(a, b):
    number_list = list(range(a, b + 1))
    number_number_list = [number for number in number_list if number % 2 == 1]
    return number_number_list
z = get_odd_number_list(1, 7)
print(z)

def get_odd_number_list_1(a, b):
    number_number_list_1 = list(range(a, b + 1))
    number_list_1 = []
    for number in number_number_list_1:
        if number % 2 == 1:
            number_list_1.append(number)
    return number_list_1
s = get_odd_number_list(1, 11)
print(s)

                                    # *args (АРГУМЕНТЫ), **kwargs (АРГУМЕНТЫ ПО КЛЮЧЕВОМУ СЛОВУ).

def then_percent_the_produkt_with_args(*args):
    product = 2 # УМНОЖАЕТ ДВА НА ПРОИЗВЕДЕНИЕ АРГУМЕНТОВ
    for number in args:
        product = number * product
    return product * 0.1 # ВОЗВРАЩАЕМ ЗНАЧЕНИЕ
print(then_percent_the_produkt_with_args(10, 20, 30))


# ДОБАВЛЯЕМ ПОЗИЦИОННЫЙ ПАРАМЕТР
def percent_the_produkt_with_args(percent, *args): # ПЕРВЫЙ ПАРАМЕТР ПОЗИЦИОННЫЙ, ВТОРОЙ ПРОИЗВОЛЬНЫЙ
    product = 1 # ОДНА ИТЕРАЦИЯ (КОЛИЧЕСТВО ИТЕРАЦИЙ)
    for number in args:
        product = product * number
    return product / 100 * percent # ВОЗВРАЩАЕМ ЗНАЧЕНИЕ, ДЕЛИМ ПРОИЗВЕДЕНИЕ НА 100 И УМНОЖАЕМ НА ПЕРВЫЙ АРГУМЕНТ(ПРОЦЕНТ)
print(percent_the_produkt_with_args(10, 10, 20, 30))


                                      #**kwargs

def greeting_keywargs(**kwargs):
    if 'name' in kwargs:
        print('Hello! Nice to meet you {}'.format(kwargs["name"]))
    else:
        print('Hellou! Whot is your name')
greeting_keywargs(name='Nikol', age='21', gender='male') # КЛЮЧОМ ДОЛЖНА БЫТЬ ВСЕГДА СТРОКА
greeting_keywargs(age='21', gender='male')

# ДОБАВЛЕНИЕ ПОЗИЦИОННОГО ПАРАМЕТРА
def greeting_keywargs(greeting, **kwargs):  # ПОЗИЦИОННЫЙ ПАРАМЕТР ДОЛЖЕН БЫТЬ ВСЕГДА ПЕРВЫМ
    if 'name' in kwargs:
        print('{}Nice to meet you {}'.format(greeting, kwargs["name"]))
    else:
        print('{}Whot is your name'.format(greeting))
greeting_keywargs(greeting='Hi!!!', name='Nikol', age='21', gender='male') # КЛЮЧОМ ДОЛЖНА БЫТЬ ВСЕГДА СТРОКА
greeting_keywargs(greeting='Hi!', age='21', gender='male')

                                 # ДОМАШНЕЕ ЗАДАНИЕ

                                 # Задача 1


def cat_is_here(*args):
    '''
    :param args Если строка 'cat' в верхнем регистре то
    :return: True без преобразования строки 'CAT' в нижний регистр
    :return: False если строка 'cat' отсутствует
    '''
    if 'cat'.upper() in args:
        return True
    elif 'cat'.lower() in args:
        return True
    else:
        return False
cat_1 = cat_is_here('CAT')
print(cat_1)
cat_2 = cat_is_here('cat')
print(cat_2)
cat_3 = cat_is_here('He is here!', 'cat')
print(cat_3)
cat_4 = cat_is_here('He is here!', 'Hi', 'By')
print(cat_4)
help(cat_is_here)


def cat_here_1(*args):
    '''
    :param Преобразование строки 'CAT' из верхнего
    в нижний регистр при помощи метода "lover"
    :return: True
    :return: False если строка 'cat' не найдена
    '''
    args_in_lower_case = [str(argument).lower() for argument in list(args)]
    if 'cat' in args_in_lower_case:
        return True
    else:
        return False
cat_5 = cat_here_1('CAT')
print(cat_5)
cat_6 = cat_here_1('cat')
print(cat_6)
cat_7 = cat_here_1('He is here!', 'cat')
print(cat_7)
cat_8 = cat_here_1('He is here!', 'Hi', 'By')
print(cat_here_1)

                                      # Задача 2
def item_is_here(item, *args):
    if item in args:
        return True
    else:
        return False
                                     # Задача 3
def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is ' + str(my_color) +
              ', but ' + kwargs['color'] + ' is also pretty good!')
    else:
        print('My favorite color is ' + str(my_color) +
              ', what is your favorite color?')
x = your_favorite_color('blue', color = 'green')
print(x)
x = your_favorite_color('green')

