print('else finaly, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
# if we have an error - exept block fires and else block dosen't fire
# if we haven' an error - else block fires and except block doesn't fire
# finally block fires anyway

# КОГДА МЫ ВВОДИМ ЗНАЧЕНИЕ В input, ТО ОНО ВОСПРИНИМАЕТСЯ КАК СТРОКА, ПОЭТОМУ ЕСЛИ М Ы ХОТИМ ЧТОБ ЧИТАЛОСЬ КАК
# ЧИСЛО, ПРИВОДИМ ВВОДИМОЕ ЧИСЛО К int.
number = input('Enter some number')

try:
    print(int(number)/2)
except:
    print('You have to enter a number!')
else:
    print('Else block')
finally:
    print('Finaly block')
print('Code after error handling')
# ДЛЯ ТОГО ЧТОБЫ ОКНО ВВОДА ВЫВОДИЛОСЬ ПОСТОЯННО ПОКА НЕ БУДЕТ ВВЕДЕНО ПРАВИЛЬНОЕ ЗНАЧЕНИЕ, МЫ ИСПОЛЬЗУЕМ ЦИКЛ WHILE
# True ОЗНАЧАЕТ, ЧТО ЦИКЛ БЕСКОНЕЧНЫЙ
while True:
    try:
        number = int(input('Enter some number'))
        print(int(number)/2)
# CРАБАТЫВАЕТ ЕСЛИ МЫ ВВЕЛИ НЕ ВЕРНОЕ ЗНАЧЕНИЕ
    except:
        print('You have to enter a number!')
# СРАБАТЫВАЕТ КОГДА МЫ ВВЕЛИ ВАЛИДНОЕ ЗНАЧЕНИЕ
    else:
        print('Good job! This is a number!')
# ВЫХОД ИЗ ЦИКЛА ПРИ ВВОДЕ ВАЛИДНОГО ЗНАЧЕНИЯ
        break
# СРАБАТЫВАЕТ ВСЕГДА, ЧАСТО ПРИМЕНЯСЯ ПРИ РАБОТЕ С ФАЙЛАМИ И ЗАКРЫВАЕТ ИХ В ЛЮБОМ СЛУЧАЕ НЕ ПОВРЕЖДАЯ ИХ
    finally:
        print('Finaly block')
    print('Code after error handling')


def divide(x, y):
    try:
        return (x / y)

    except ZeroDivisionError as e:
        print('You can\'t divide by zero!')
        print(e)
# as and e ДОЛЖНЫ ВЫВОДИТ ОБЬЯСНЕНИЕ САМОЙ ОШИБКИ
    except TypeError as e:
        print('x and y must be numbers')
        print(e)
    else:
        print('x was divided by y')
    finally:
        print('Finally block')

print(divide(1000, 0))