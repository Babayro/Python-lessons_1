# УСЛОВНЫЕ ОЕРАТОРЫ if (ЕСЛИ), elif(ИНАЧЕ, ЕСЛИ), else (ИНАЧЕ)
# ВЕТОК elif МОЖЕТ БЫТЬ СКОЛЬКО УГОДНО
условные_операторы = 'УСЛОВНЫЕ ОПЕРАТОРЫ if, elif, else РЕЗУЛТАТ РАБОТЫ ПРОГРАММЫ'
name = 'Viktor'
age = 19
is_married = False
if age > 18 and is_married == False:
    print('Hi {}! You can fine a gerl of your dream here!'.format(name))
elif age < 18 or is_married == True:
    print ('СОСИ!')
# ЕСЛИ НЕ СРАБАТЫВАЕТ if и elif  ТО ВЫПОЛНЯЕТСЯ else
# ОТСТУП С ВЫПОЛНЯЕМЫМ БЛОКОМ КОДА В ОТЛИЧАЕ ОТ ДРУГИХ ЯЗЫКОВ ПРОГРАММИРОВАНИЯ ВЫДЕЛЯЕТСЯ НЕ { }, А ОТСТУПАМИ
# ЕСЛИ НЕ УКАЗАТЬ  else ТО ПОСЛЕДНИЙ БЛОК КОДА (ТАМ ГДЕ ДОЛЖЕН БЫТЬ else) ТОЖЕ ВЫПОЛНИТСЯ.
x = 4
if x > 3:
    print('x > 3')
# МОЖНО ВЫПОЛНИТЬ НЕ ОДНУ СТРОЧКУ КОДА
    print('i\'am happy')
# УСЛОВНЫЕ ОПЕРАТОРЫ ОБЯЗАТЕЛЬНО ПЕЧАТАЕМ В НАЧАЛЕ СТРОКИ ИНАЧЕ БУДЕТ ОШИБКА
elif x < 3:
    print('x < 3')
else:
    print('x == 3')

# ПРИМЕР ИСПОЛЬЗОВАНИЯ elif В БОЛЬШОМ КОЛИЧЕСТВЕ
day_time = 'midniht'
if day_time == 'morning':
    print('Monster wake up')
elif day_time == 'afternoon':
    print('Monster is wolking')
elif day_time == 'evening':
    print('Monster is eating')
elif day_time == 'nith':
    print('Monster is sleeping')
else:
    print('Monster something')

# МЫ МОЖЕМ ИСПОЛЬЗОВАТЬ ТОЛЬКО ЧАСТЬ if и else В СЛУЧАЕ ЕСЛИ ЕСТЬ ТОЛЬКО ДВА ВАРИАНТА РАЗВИТИЯ
x = 40
if x % 2 == 0:
    print ('x is even')
else:
    print('x is odd')
# ПОСЛЕ ЭТОГО КОДА С ОПЕРАТОРАМИ МОЖЕТ ВЫВОДИТЬСЯ ЛЮБОЙ КОД БЕЗ ОТСТУПА ОТ КРАЯ СТРОКИ
# else МОЖНО ВСТАВЛЯТЬТОЛЬКО ОДИН РАЗ, Т.К. ОН СРАБАТЫВАЕТ В СЛУЧАЕ ПОЛНОГО НЕВЫПОЛНЕНИЯ УСЛОВИЙ.
print('some text')

# ПРИМЕР ИСПОЛЬЗОВАНИЯ ТОЛЬКО if
# ПРИМЕНЯЕМ ФУНКЦИЮ input (ОНА СОЗДАЁТ ОКНО ВВОДА В БРУЗЕРЕ!!!)
user_input = input('input user text')
if user_input == 'Hi':
   print('Welkome user!')

# False всегда будет if = 0, '',[], None
if 1:
    print('Some text')

lucki_number = input('Enter a number')
if lucki_number:
    print(lucki_number + ' is you lucki number')
else:
    print('You have to enter some number, please try again!')

# ДОМАШНЕЕ ЗАДАНИЕ
# ЗАДАЧА 1
any_number = input('Enter any number')
if any_number == '7':
     print(any_number + ' is a lucky number! Today is your lucky day!')
else:
    print('Thank you! Have a nice day!')

# ЗАДАЧА 2

user_input = input('Enter an integer number')
if user_input % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')