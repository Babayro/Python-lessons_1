print('iterable and iterator, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')

                          # Itarable - ЭТО ПЕРЕБИРАЕМЫЕ ОБЪЕКТ

number_list = [1, 2, 3, 4 , 5, 6, 7]

for number in number_list:
    print(number)

for letter in 'My string':
    print(letter)

                # Iterator - ЭТО ПЕРЕБОЩИК И ЕГО МОЖНО ПОЛУЧИТЬ ИЗ ПРИ ПОМОЩИ МЕТОДА iter ИЗ ПЕРЕБИРАЕМОГО ОБЪЕКТА

number_list_iterator = iter(number_list)
# ПОЛУЧАЕМ КЛАСС iterator
print(type(number_list_iterator))
print(number_list_iterator)

string_iterator = iter('My string')
print(type(string_iterator))

    # ОБЪЕКТЫ itarable ПЕРЕБТРАЮТСЯ ПРИ ПОМОЩИ iterator, А ДЛЯ ПЕРЕБОРА В ИТЕРАТОРЕ ВЫЗЫВАЕТСЯ МЕТОД NEXT
    # КАЖДЫЙ РАЗ ВЫЗЫВАЯ МЕТО  next МЫ БУДЕМ ПЕРЕХОДИТЬ К СЛЕДУЮЩЕМУ ЭЛЕМЕНТУ ПОСЛЕДОВАТЕЛЬНОСТИ
    # ПОСЛЕ ВЫВОДА ПОСЛЕДНЕГО ЭЛЕМЕНТА ПРОИЗОЙДЁТ ОШИБКА stop iterate ИМЕННО ЭТО И ПРОИСХОДИТ В ЦИКЛАХ
print(number_list_iterator.__next__())
print(number_list_iterator.__next__())
print(number_list_iterator.__next__())
print(number_list_iterator.__next__())


    # ТАКЖЕ ПОМИМО МЕТОДА next, МЫ МОЖЕМ ИСПОЛЬЗЫВАТЬ ФУНКЦИЮ next ДЛЯ ПЕРЕДАЧИ В НЕЁ НУЖНЫХ НАМ ПАРАМЕТРОВ
    # В ДАННОМ СЛУЧАЕ  МЫ ПОМЕСТИМ В ФУНКЦИЮ ИТЕРАТОР
print(next(number_list_iterator))
print(next(string_iterator))

# НА ПРИМЕРЕ ФУНКЦИИ
def my_for_loop(iterable):
    iterator = iter(iterable)
    print(iterator.__next__())
    print(iterator.__next__())
# ТАКЖЕ МОЖНО ИСПОЛЬЗОВАТЬ ФУНКЦИЮ next
    print(next(iterable))
# ПОЛУЧАЕМ ПЕРВУЮ БУКВУ СТРОКИ
# my_for_loop('hello')

# МОЖЕМ ВЫВЕСТИ ВСЕ ЭЛЕМЕНТЫ С ПОМОЩЬЮ ЦИКЛА И ПРЕРВАТЬ ЕГО В ВИДЕ ОШИБКИ ПОСЛЕ ВЫВОДА ПОСЛЕДНЕГО ЭЛЕМЕНТА
# ЧТОБЫ НЕ БЫЛО ОШИБКИ МЫ ЗАВЕРНЕМ ЦИКЛ В БЛОК true except
def my_for_loop_1(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('Iteration is finisht')
            break

my_for_loop_1('Simpsons')
my_for_loop_1([1, 2, 3, 4, 5, 6, 7])