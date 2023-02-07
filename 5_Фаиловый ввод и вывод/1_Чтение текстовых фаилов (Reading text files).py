gtgryhtyj = 'ЧТЕНИЕ ТЕКСТОВЫХ ФАИЛОВ (READING TEXT THE FILES ) , РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(gtgryhtyj)
# ВВОД ВЫВОД ТЕКСТА В ТЕРМИНАЛЕ
# input
x = input('input something')
# output
print('Output something' + x)
# МЫ МОЖЕМ ВВОДИТЬ И ВЫВОДИТЬ ИНФОРМАЦИЮ НЕ В ТЕРМИНАЛЕ, А В ФАИЛ И ИЗ ФАИЛА
# ПАРАМЕТРЫ ФУНКЦИИ print, end по умолчанию равен = '\n'(ПЕРЕНОС СТРОКИ)
print(1, 2, 3, sep=':', end='\n')
print(1,2,3, sep=',', end=' ')
print(1,2,3, sep=';', end='')
print('')

# ОТКРЫВАЕМ ФАИЛ С ТЕКСТОМ И ПОМЕЩАЕМ ЕГО В ПЕРЕМЕННУЮ lorem_ipsum_text, r ОЗНАЧАЕТ, ЧТО МЫ БУДЕМ ТОЛЬКО ЧИТАТЬ ИЗ ЭТОГО ФАИЛА
lorem_ipsum_text = open('/home/silistin/Рабочий стол/sample.txt', 'r')
# ВЫВОДИМ С ПОМОЩЬЮ ЦИКЛА ТЕКСТ В ПЕРЕМЕННУЮ line
for line in lorem_ipsum_text:
    print(line, end='') # ДОБАВЛЯЕМ В end ПУСТУЮ СТРОКУ ЧТОБЫ СТРОКИ БЫЛИ БЕЗ ПРОМЕЖУТКОВ, Т.К. ПРИНТ ВЫЗЫВАЕТ ДОП ПРОМЕЖУТОК И В ФАИЛЕ КОНЕЦ СТРОКИ ЭТО ПЕРЕНОС
# ЗАКРЫВАЕМ ОСНОВНУЮ ПЕРЕМЕННУЮ С ТЕКСТОМ
lorem_ipsum_text.close()
print('\n')
# РАСПЕЧАТЫВАЕМ ТОЛЬКО ТЕ СТРОКИ В КОТОРЫХ ЕСТЬ СЛОВО let
lorem_ipsum_text = open('/home/silistin/Рабочий стол/sample.txt', 'r')
for line in lorem_ipsum_text:
    if 'mary' in line.lower():
        print(line, end='')
lorem_ipsum_text.close()# ОБЯЗАТЕЛЬНО ЗАКРЫВАТЬ ФАИЛЫ ИНАЧЕ ОНИ МОГУТ БЫТЬ ПОВРЕЖДЕННЫ

                             #   ОТКРЫТИЕ ФАИЛА
# ОТКРЫТЫЙ ТАКИМ ОБРАЗОМ ФАИЛ НЕ НУЖНО ЗАКРЫВАТЬ, ОН ЗАКРОЕТСЯ САМ АСТОМАТИЧЕСКИ ПРИ ПОМОЩИ МЕТОДА with
with open('/home/silistin/Рабочий стол/sample.txt', 'r') as lorem_ipsum_text:
    for line in lorem_ipsum_text:
        if 'mary' in line.lower():
            print(line, end='')
print('\n')
                              #РАСПЕЧАТКА ОТДЕЛЬНЫХ СТРОК ПРИ ПОМОЩИ МЕТОДА readline
with open('/home/silistin/Рабочий стол/sample.txt', 'r') as lorem_ipsum_text:
    line = lorem_ipsum_text.readline()
    print(line)# РАСПЕЧАТАЕТ ПЕРВУЮ СТРОКУ

print('\n')

with open('/home/silistin/Рабочий стол/sample.txt', 'r') as lorem_ipsum_text:
    line = lorem_ipsum_text.readline()# МЕТОД readline ЧИТАЕТ ОДНУ СТРОКУ
    while line:
        print(line, end='')
        line = lorem_ipsum_text.readline()

print('\n')
                                      # ПОЛУЧАЕМ СПИСОК СТРОК ИЗ ФАИЛА
with open('/home/silistin/Рабочий стол/sample.txt', 'r') as lorem_ipsum_text:
    line = lorem_ipsum_text.readlines()
# ВЫХОДИМ ИЗ ОПЕРАТОРА with, ПЕРХОДИМ К НАЧАЛУ СТРОКИ И РАСПЕЧАТЫВАЕМ СПИСОК В ПЕРЕМЕННОЙ line
print(line)
print(line[0:3])

print('\n')

# МЕТОД readlines ЧИТАЕТ ВСЕ СТРОКИ ФАИЛА И ПОМЕЩАЕТ ИХ В СПИСОК
with open('/home/silistin/Рабочий стол/sample.txt', 'r') as lorem_ipsum_text:
    line = lorem_ipsum_text.readlines()
    for num_line in line [0:3]:
        print(num_line, end='')


print('\n')

                               # МЕТОД read РАСПЕЧАТЫВАЕТ ВЕЬ ФАИЛ
with open('/home/silistin/Рабочий стол/sample.txt', 'r') as lorem_ipsum_text:
    line = lorem_ipsum_text.read()
print(line)
# ЧТОБЫ НЕ ПЕРЕГРУЖАТЬ ПАМЯТЬ КОМПЬЮТЕРА ЛУЧШЕ ЧИТАТЬ ФАИЛ ПОСТРОЧНО ПРИ ПОМОЩИ МЕТОДА readline



