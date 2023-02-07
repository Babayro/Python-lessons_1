print('ВЫЗОВ ОШИБОК, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
def get_rainbow_color(color_number):
# ОБЯЗАТЕЛЬНО СОЗДАЁМ ДОКУМЕНТАЦИЮ В ОПИСАНИЕМ РАБОТЫ ОШИБОК
'''

:param color_number: Color number must be integer type
and Color number must be in range of integer from 1 to 7
:return:
'''

# СОЗДАЁМ ОШИБКУ ЕСЛИ ВМЕСТО ЧИСЛА ВВЕДУТ СТРОКУ
    if type(color_number) is not int:
        raise TypeError('Color number must be integer type')
# СОЗДАЁМ ОШИБКУ КОТОРУЮ ВЫБРОСИТ ЕСЛИ ЧИСЛО БУДЕТ ОТСУТСТВОВАТЬ В ДИАПАЗОНЕ ЧИСЕЛ
    color_number_list = [1, 2 , 3, 4, 5, 6, 7]
    if color_number_list not in color_number_list:
# raise КЛЮЧЕВОЕ СЛОВО СОЗДАНИЯ ОШИБКИ, not in
        raise ValueError('Color number must be in range of integer from 1 to 7')
    if color_number == 1:
        return 'red'
    elif color_number == 2:
        return 'orange'
    elif color_number == 3:
        return 'yellow'
    elif color_number == 4:
        return 'green'
    elif color_number == 5:
        return 'blue'
    elif color_number == 6:
        return 'indigo'
    elif color_number == 7:
        return 'violet'

color = get_rainbow_color(1.0)
print(color)