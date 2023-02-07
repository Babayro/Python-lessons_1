v = 'ЛЯМБДА ВЫРАЖЕНИЯ, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'

                                         # Функция Map
# Эта функция которая ВКЛЮЧАЕТ В СЕБЯ ФУНКЦИЮ И ОБЪЕКТ ДЛЯ РАБОТЫ
def sum_of_two_numbers(x):
    return x + x

number_list = [1, 2 ,3 ,4 ,6 , 7]

# В map помещаем функцию и список с которым будем работать
result = map(sum_of_two_numbers, number_list)
print(result)

for item in result:
    print(item)

# Более простая запись
for item in map(sum_of_two_numbers, number_list):
    print(item)
# ВЫВОД СПИСКА
print(list(map(sum_of_two_numbers, number_list)))

# ИЩИМ НУЖНУЮ БУКВУ
def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False
string_list = ['werhg', 'asdfgh', 'wertyu', 'gfdsa']

print(list(map(is_a_in_string, string_list)))

                                           # Функция filter ПЕРЕМЕЩАЕТ В НОВУЮ ПОЛЕДОВАТЕЛЬНОСТЬ ОБЪЕКТЫ С РЕЗУЛЬТАТОМ True
def is_number_odd(number):
    return number % 2 == 1


number_list = [1, 2, 3, 4, 5, 6, 7]
# ВЫВОДИТ ОБЪЕКТ С НОМЕРОМ В ПАМЯТИ
print(filter(is_number_odd, number_list))
# ВЫВОДИТ СПИСОК
print(list(filter(is_number_odd, number_list)))

#ВЫВОДИТ ПОСЛЕДОВАТЕЛЬНОСТЬ НЕЧЁТНЫХ ЧИСЕЛ
for number in filter(is_number_odd, number_list):
    print(number)

# ПОЛУЧАЕМ ТЕ СТРОКИ КОТОРЫЕ СОДЕРЖАТ БУКВУ "a"
def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False
string_list = ['werhg', 'asdfgh', 'wertyu', 'gfdsa']

print(list(filter(is_a_in_string, string_list)))

                # Lambda Exspression ФУНКЦИЯ БЕЗ ИМЕНИ КОТОРАЯ ВЫЗЫВАЕТСЯ ВСЕГО ЛИШЬ ОДИН РАЗ (ВСЕГДА ВОЗВРАЩАЕТ ЗНАЧЕНИЕ)
def cube(number):
    return number ** 3
number_list = [1, 2 , 3, 4, 5, 6, 7]
print(list(map(lambda number: number ** 3, number_list)))

print(list(filter(lambda number: number % 2 == 0, number_list)))
print(list(filter(lambda number: number % 2 == 1, number_list)))