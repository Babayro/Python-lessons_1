import time

print('Generator expressions, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')

# СОЗДАНИЕ ГЕНЕРАТОРОВ ПРИ ПОМОЩИ ВЫРАЖЕНИЙ

# ГЕНЕРАТОР СОЗДАННЫЙ ПРИ ПОМОЩИ ФУНКЦИИ
def get_number_from_range():
    for number in range(10):
        yield number
# ЕСЛИ ПРИНТОВ БУДЕТ БОЛЬШЕ ТО ВЫЛЕЗЕТ ОШИБКА StopIteration
counter = get_number_from_range()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

try:
    print(StopIteration)
    print(next(counter))
except TypeError:
    StopIteration
    print(next(counter))
except TypeError:
    StopIteration

# УКОРОЧЕННАЯ ЗАПИСЬ, ГЕНЕРАТОР СОЗДАННЫЙ ПРИ ПОМОЩИ ВЫРАЖЕНИЯ
counter_1 = (number_1 for number_1 in range(10))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))


# ПОЛУЧАЕМ СПИСОК, И ЗАНИМАЕМ ПАМЯТЬ
print(sum([number for number in range(10)]))
# ПОЛУЧАЕМ ГЕНЕРАТОР И НЕ ЗАНИМАЕМ ПАМЯТЬ
print(sum((number for number in range(10))))

                                         # ИЗМЕРЯЕМ ВРЕМЯ ОБРАБОТКИ ПРИ ПОМОЩИ ЛИСТА И ГЕНЕРАТОРА
# ФУНКЦИЯ time ОБРАБАТЫВАЕТ ТЕКУЩИЙ МОМЕНТ ВРЕМЕНИ, А sum СКЛАДЫВАЕТ ВСЕ ЭЛЕМЕНТЫ СПИСКА

list_start_time = time.time()
print(sum([number_3 for number_3 in range(1000000)]))
list_processing_time = time.time() - list_start_time

gen_start_time = time.time()
print(sum((number_3 for number_3 in range(1000000))))
gen_processing_time = time.time() - gen_start_time

print(f'Processing with list is {list_processing_time}')
print(f'Processing with gen is {gen_processing_time}')