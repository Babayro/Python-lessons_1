логические_операторы = 'ЛОГИЧЕСКИЕ ОПЕРАТОРЫ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(логические_операторы)
x = 1
y = 2

print(x > 1)
print(y > 1)
# ЧТОБЫ УЗНАТЬ ОБ ИСТИННОСТИ ЭТИХ ВЫРАЖЕНИЙ СУЩЕСТВУЕТ ЛОГИЧСКИЙ ОПЕРАТОР
# СУЩЕТСВУЕТ ТРИ ОСНОВНЫХ ЛОГИЧЕСКИХ ОПЕРАТОРА: and, or (или), not
# В НИЖНЕМ ВЫРАЖЕНИИ МЫ ХОТИМ ЧТОБЫ X И Y = 1, Т.К. ЭТО НЕ ТАК БУДЕТ False
print(x > 1 and y > 1)
# ЕСЛИ X  ИЛИ Y > 1  ТО БУДЕТ True
print(x > 1 or y > 1)
# Т.К. X НЕ > 1 ВЕРНЁТ True
print(not x > 1)
# БУДЕТ False Т.К. Y > 1
print(not y > 1)
print(True and True)
print(True or True)
print(not True)

print(False and False)
print(False or False)
print(not False)

print(True and False)
print(True or False)

# ПРИМЕР: НА САЙТЕ ЗНАКОМСТВ ЕСТЬ ДАННЫЕ ПОЛЬЗОВАТЕЛЯ
name = 'Viktor'
age = 14
is_married = False
if age > 18 and is_married == False:
    print('Hi {}! You can fine a gerl of your dream here!'.format(name))