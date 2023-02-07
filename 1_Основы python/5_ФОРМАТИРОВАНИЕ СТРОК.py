#2.3.ФОРМАТИРОВАНИЕ СТРОК
form_string = 'ФОРМАТИРОВАНИЕ СТРОК, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(1 + 1)
#ПОЛУЧАЕМ СЛОЖЕНИЕ СТРОК ПРИ ПОМОЩИ КОНКАТЕНАЦИИ
print('1' + "1")
age = 23
#БУДЕТ ОШИБКА Т.К. СТРОКИ МОЖНО КОНКАТЕНИРОВАТЬ ТОЛЬКО СО СТРОКАМИ, А НЕ С ЧЕЛЫМИ ЧИСЛАМИ
#print('Jake' + age + 'yers old.')
# age ПРИВОДИМ К ТИПУ STRING (ИСПОЛЬЗУЕМ ПРОБЕЛ ОТ ПЕРВЫХ КАВЫЧЕК В СТРОКАХ ДЛЯ РАЗДЕЛЕНИЯ СЛОВ)
print('Jake ' + str(age) + ' yers old.')

#МОЖЕМ ПОМЕСТИТЬ СРАЗУ ЗНАЧЕНИЕ, А НЕ ПЕРЕМЕННУЮ
print('Jake ' + str(23) + ' yers old.')
#Если у нас много значений, то конкатенация не эффективна,есть другой способ
name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\' am {1} yers old'.format(name, age)
print(name_and_age)
name_and_age = 'My name is {0}. I\' am {1} yers old'.format('Jack',23)
print(name_and_age)
name_and_age = 'My name is {}. I\' am {} yers old'.format(23, 'Jack')
print(name_and_age)
#ВЫВОДИМ ДНИ НЕДЕЛИ ЧЕРЕЗ УКАЗАНИЕ ИНДЕКСОВ НАЧИНАЯ С 0
week_days = 'There are 7 days a week: {5}, {0}, {3}, {1}, {2}, {4},{6}.'\
    .format('Monday','Wednesday', 'Thursday', 'Tuesday','Friday', 'Sunday', 'Saturday')
print(week_days)

#ПРИСВОЕНИЕ КЛЮЧЕЙ
week_days = 'There are 7 days a week: {su}, {mo}, {tu}, {we}, {th}, {fr},{sa}.'\
    .format(mo = 'Monday',we = 'Wednesday',th = 'Thursday',tu = 'Tuesday',fr = 'Friday',su = 'Sunday',sa = 'Saturday')
print(week_days)

#ВЫВОДИМ НЕСКОЛЬКО РАЗ ПОДРЯД ВОСКРЕСЕНЬЕ
week_days = 'There are 7 days a week: {sa}, {sa}, {sa}, {sa}, {sa}, {sa},{sa}.'\
    .format(mo = 'Monday',we = 'Wednesday',th = 'Thursday',
            tu = 'Tuesday', fr = 'Friday',
            su = 'Sunday', sa = 'Saturday')
print(week_days)
# СОКРАЩАЕМ КОЛИЧЕСТВО СИМВОЛОВ ПОСЛЕ ТОЧКИ
# УКАЗЫВАЕМ ЛЮБОЕ КОЛИЧЕСТВО СИМВОЛОВ ДО ТОЧКИ, УКАЗЫВАЕМ КОЛИЧЕСТВО СИМВОЛОВ ПОСЛЕ ТОЧКИ КОТОРЫЕ ХОТИМ ОСТАВИТЬ
float_result = 1000 / 7
print(float_result)
print('The result of division is {0:1.3f})'.format(float_result))

# ЕСЛИ УКАЗАТЬ ЧИСЛО КОТОРОЕ БОЛЬШЕ КОЛИЧЕСТВА СИМВОЛОВ ДО ТОЧКИ, ТО ПРИ ВЫВОДЕ ПЕРЕД ЧИСЛОМ В СТРОКЕ БУДЕТ ПРОБЕЛ
# ЭТО МОЖЕТ ПРИГОДИТЬСЯ ПРИ ВЫВОДЕ ЧИСЕЛ В ВИДЕ ТАБЛИЦЫ
float_result = 1000 / 7
print(float_result)
print('The result of division is {0:10.3f})'.format(float_result))

#ВЫВОД ТАБЛИЦЫ
#ПЕРВЫЙ СИВОЛ В СКОБКАХ ЭТО ПОРЯДКОВЫЙ НОМЕР ВЫВОДА ЧИСЛА,
#ВТОРОЙ СИМВОЛ "10" ЭТО ПРОБЕЛ Т.К. ОНО БОЛЬШЕ КОЛИЧЕСТВА СИМВОЛОВ ДО ТОЧКИ
#2f КОЛИЧЕСТВО СИМОВЛОВ ПОСЛЕ ТОЧКИ

print('''
{0:10.2f} {1:10.2f} {2:10.2f}
{3:10.2f} {4:10.2f} {5:10.2f}
{6:10.2f} {7:10.2f} {8:10.2f}
'''.format(1.23565, 45.12355, 23.236589123, 23.23654, 78.236657, 3.12354,
21.2365, 1236.456, 125.256))

#ФОРМАТИРОВАНИЕ СТРОКОВЫХ ЛИТЕРАЛОВ
name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\' am {1} yers old'.format(name, age)

# СТАВИМ "F" ПЕРЕД СТРОКОЙ, ВМЕСТО ВЫЗОВА МЕТОДА ЧЕРЕЗ ТОЧКУ
name_and_age = f'My name is {name}. I\' am {age} yers old'
print(name_and_age)

#СТАРЫЙ СПОСОБ НЕ РЕКОМЕНДУЕТСЯ К ИСПОЛЬЗОВАНИЮ И СКОРО БУДЕТ ЗАПРЕЩЁН!!!
# % s.=строка(name),следущие методы без точек %d = число 23, перечисляем параметры
print('My name is %s. i\' am %d yers old' % (name, age))
print('My name is %s. %s %d yers old' % (name, "i'am", age))