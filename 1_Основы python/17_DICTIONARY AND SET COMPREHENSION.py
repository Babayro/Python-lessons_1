dictionary_and_set_comprehension = 'Dictionary and Set Comprehension РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
# ТАКЖЕ КАК И С ЛИСТАМИ СО СЛОВАРЯМИ МЫ ТАКЖЕ МОЖЕМ ИСПОЛЬЗОВАТЬ БОЛЕЕ КОРОТКОЮ ФОРМУ ЗАПИСИ
# ВОЗВОДИМ ЗНАЧЕНИЯ СЛОВАРЯ В СТЕПЕНЬ 3
number_dict = {'first': 1, 'second': 2, 'third': 3 }
new_dict = {key: value ** 3 for key, value in number_dict.items()}
print(new_dict)

# ПОЛУЧЕНИЕ ИЗ СПИСКА НОВОГО СЛОВАРЯ С ВОЗВЕДЕННЫМИ ИЗ СПИСКА В СТЕПЕНЬ 2 ЗНАЧЕНИЙ,
# ИЗНАЧАЛЬНЫЕ ЗНАЧЕНИЯ СПИСКА В ЭТОМ СЛУЧАЕ БУДУТ ЯВЛЯТЬСЯ КЛЮЧАМИ, А ИХ СТЕПЕНЬ БУДЕТ ЗНАЧЕНИЕМ
number_list = [1, 2, 3, 4, 5]
number_dict_2 = {number: number ** 2 for number in number_list}
print(number_dict_2)

# ПОДПИСЫВАЕМ И ВЫВОДИМ ОТРИЦАТЕЛЬНЫЕ И ПОЛОЖИТЕЛЬНЫЕ ЗНАЧЕНИЯ ИЗ ЛИСТА В СЛОВАРЬ
number_list = [1, 2, -2, -64, 98, 21, -98, 0]
number_dict_2 = {number: 'positive' if number > 0
else 'negative' if number < 0 else 'zero' for number  in number_list}
print(number_dict_2)
# ВЫВОДИМ СПИСОК С - И +
number_dict_2 = {number: '+' if number > 0
else '-' if number < 0 else 'zero' for number  in number_list}
print(number_dict_2)

# Set Comprehension ПРЕОБРАЗОВАНИЕ ЛИСТА В МНОЖЕСТВО
number_list = [1, 2, -2, -64, 98, 21, -98, 0]
number_set = {number ** 2 for number in number_list}
print(number_set)
# СОЗДАНИЕ МНОЖЕСТВА В ДИАПАЗОНЕ
number_set = {number ** 2 for number in range(1, 55)}
print(number_set)

# ПРЕОБРАЗОВАНИЕ СТРОКИ В МНОЖЕСТВО.!!!СТРОКА СТАНОВИТСЯ НЕУПОРЯДОЧЕННОЙ ПОСЛЕДОВАТЕЛЬНОСТЬЮ, МНОЖЕСТВОМ!!!
letter_set = {letter for letter in 'Pososi'}
print(letter_set)
# ДЕЛАЕМ БУКВА В МНОЖЕСТВЕ ЗАГЛАВНЫМИ
letter_set = {letter.upper() for letter in 'Pososi'}
print(letter_set)