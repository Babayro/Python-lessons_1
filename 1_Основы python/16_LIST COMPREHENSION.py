list_com = 'list comprehension РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(list_com)
# List comprehension  - ЭТО КОНЦЕПЦИЯ О ТОМ КАК МОЖНО СОЗДАВАТЬ СПИСКИ ИЗ РАЗЛИЧНЫХ ПОСЛЕДОВАТЕЛЬНОСТЕЙ
# ПРИ ПОМОЩИ ЭЛЕГАНТНОЙ И БОЛЕЕ КОРОТКОЙ ФОРМЫ ЗАПИСИ
# НАПРИМЕР МОЖНО СОЗДАТЬ СПИСОК ИЗ КАКОЙ-ТО ПОСЛЕДОВАТЕЛЬНОСТИ ПРИ ПОМОЩИ ЦИКЛА
greeting = 'Hello!!!'
letter_list = []
for letter in greeting:
    letter_list.append(letter)
    print(letter_list)
# !!!НИЖЕ ПРИВЕДЁННЫЕ ЗАПИСИ И КОМАНДЫ К НИМ, ЗАПИСЫВАЮТСЯ С ВОЗВРАТОМ КАРЕТКИ БЕЗ ТАБУЛЯЦИИ!!!
# ТОЖЕ САМОЕ ТОЛЬКО С ИСПОЛЬЗОВАНИЕМ БОЛЕЕ КОРОТКОЙ ФОРМЫ ЗАПИСИ
# ДАННЫЙ КОД НУЖНО ЧИТАТЬ НАЧИНАЯ С for
greeting_2 = "Hello elephant"
letter_list_2 = [letter_2 for letter_2 in greeting_2]
print(letter_list_2)

# ВЫВОД ЧИСЛОВОГО, СТРОЧНОГО ЛИСТА ИЗ СТРОКИ С ЦИФРАМИ
number_list = [number for number in '123456789']
print(number_list)

# ПОЛУЧЕНИЕ ЧИСЛОВОГО СПИСКА С ПРИМИНЕНИЕМ ФУНКЦИИ range
number_list_4 = [number_4 for number_4 in range(1, 5)]
print(number_list_4)

# ПОЛУЧАЕМ РЕЗУЛЬТАТЫ ВОЗВЕДЕНИЯ ЧИСЕЛ В КВАДРАТ ИЗ ЗАДАННОГО ДИАПАЗОНА range
number_list_5 = [num ** 2 for num in range(1, 5)]
print(number_list_5)

# СОЗДАЁМ СПИСОК ТОЛЬКО ИЗ ПОЛОЖИТЕЛЬНЫХ ЧИСЕЛ
number_list_6 = [-2, -65, 12, 69, 72, 69, -87]
new_number_list = [number for number in number_list_6 if number > 0 ]
print(new_number_list)

#ПЕРЕД ПОМЕЩЕНИЕМ В СПИСОК МЫ МОЖЕМ ПРОИЗВОДИТЬ КАКИЕТО ДЕЙСТВИЯ С ОБЪЕКТОМ
number_list_7 = [12, -21, 36, -32, 87, -65]
new_list_7 = [number_7 ** 3 / 2 for number_7 in number_list_7]
print(new_list_7)
# СОЗДАЁМ ЛИСТ ТОЛЬКО С - И +
new_list_8 = ['+' if number_7 > 0 else '-' for number_7 in number_list_7]
print(new_list_8)

# ДОМАШНЕЕ ЗАДАНИЕ
# ЗАДАЧА 1
# Без list comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
new_greetings_list = []
for new_letter in greetings:
    new_greetings_list.append(new_letter [1])
print(new_greetings_list)

# C list comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
new_gretting_list = [new_letter [1] for new_letter in greetings]
print(new_gretting_list)

# Задача 2
# Без list comprehension
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letter_list = []
for odd_numbers in digits:
      if odd_numbers % 2 == 1:
       letter_list.append(odd_numbers)
       print(letter_list)

# C list comprehension
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [numbers_2 for numbers_2 in digits if numbers_2 % 2 == 1]
print(odd_numbers)