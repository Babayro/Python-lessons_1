print('try except РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
# В ЭТОМ КОДЕ МЫ РАССМОТРИМ КАК МОЖНО УПРАВЛЯТЬ ОШИБКАМИ
# ВЫПОЛНЯЕТСЯ

print('Some code')
# ОШИБКА, АВАРИЙНА ОСТАНОВКА, Т.К. МЫ ПЫТАЕМСЯ РАСПЕЧАТАТЬ ПЕРЕМЕННУЮ КОТОРОЙ НЕТ
# ДЛЯ ТОГО, ЧТОБЫ В СЛУЧАЕ ВОЗНИКНОВЕНЯ ПОТЕНЦИАЛЬНОЙ ОШИБКИ КОД ИСПОЛНЯЛСЯ ДАЛЬШЕ, МЫ ИСПОЛЬЗУЕМ СПЕЦИАЛЬНУЮ КОНСТРУКЦИЮ
try:
# ЕСЛИ ПОМЕНЯТЬ МЕСТАМИ НИЖНИЕ ПРИНТЫ ТО БУДЕТ ВЫВОДИТСЯ НАЗВАНИЕ ОШИБКИ ВЕРХНЕГО ПРИНТА
    print('Some code')
    print(my_variable)
    print(len(23))
except NameError:
    print('NameError error a happen')
# МЫ МОЖЕМ ДЛЯ РАЗНЫХ ПОТЕНЦИАЛЬНЫХ ОШИБОК СОЗДАТЬ НЕСКОЛЬКО БЛОКОВ except
# НЕ ВЫПОЛНЯЕТСЯ
except TypeError:
    print('TypeError has happen')
print('Code after error')

# ТОЖЕ САМОЕ НА ПРИМЕРЕ ФУНКЦИИ
user_dictionary = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}
print(user_dictionary['last_name'])
# БУДЕТ ОШИБКА NameError
# print(user_dictionary['cat'])
# НО ЕСЛИ МЫ УЖЕМ МЕТОД   get И УКАЖЕМ НЕ ВАЛИДНЫЙ КЛЮЧЬ ТО МЫ ПОЛУЧИМ НЕ ОШИБКУ, А None, Т.К. НЕ ВАЛИДНЫЙ КЛЮЧ НИЧЕГО НЕ ВОЗВРАЩАЕТ
# НО ЕСЛИ МЫ УКАЖЕМ В МЕТОДЕ get НЕ СТРОКУ, А ЧИСЛО ТО БУДЕТ ОШИБКА, А НЕ ПУСТОЕ ЗНАЧЕНИЕ None
print(user_dictionary.get('last_name'))
print(user_dictionary.get('cat'))

# ПРИМЕР ФУНКЦИИ
def get_dictionary_values(dictionary, key):
    '''
    if dictionary haven't specified key, the function returns None
    :param dictionary:
    :param key:
    :return:
    '''
    try:
        return dictionary[key]
    except KeyError:
        return None
print(get_dictionary_values(user_dictionary, 'age'))
print(get_dictionary_values(user_dictionary, 'cat'))