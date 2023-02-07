tema = 'ТЕМА СТРОКИ Indexing & Slicing РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(tema)
#Indexing
#КОМАНДА ДЛЯ ВЫВОДА КОЛИЧЕСТВА СИМВОЛОВ В СТРОКЕ НАЧИНАЯ С 0
greeting = 'Hello Python!'
greeting_length = len(greeting)
print(greeting_length)
#ТОЖЕ САМОЕ ТОЛЬКО  С ПРЯМЫМ ВЫВОДОМ КОМАНДЫ, А НЕ ПЕРЕМЕННОЙ
greeting_length = len(greeting)
print(len(greeting))
#ВЫВОД СИМВОЛА ПО ЕГО НОМЕРУ В СТРОКЕ(13-Й СИМВОЛ ЭТО СИМВОЛ "!")
print(greeting[0])
print(greeting[6])
print(greeting[8])
#ВЫВОД ЭЛЕМЕНТОВ С КОНЦА СТРОКИ (ПОСЛЕДНИЙ ЭЛЕМЕНТ СТРОКИ ТАКЖЕ СЧИТАЕТСЯ КАК [0], ЗАТЕМ [-1]
print(greeting[-1])
print(greeting[-4])

#Slicing-ВЫРЕЗАНИЕ ЭЛЕМЕНТА СТРОКИ
#С НАЧАЛО УКАЗЫВАЕМ ИНДЕКС ПЕРВОГО ЭЛЕМЕНТА, ЗАТЕМ ИНДЕКС ЭЛЕМЕНТА ДО КОТОРОГО ВЫРЕЗАЕМ
print(greeting[2:5])
print(greeting[6:13])
print(greeting[0:5])
print(greeting[1:6])
print(greeting[0:7])

#ВЫРЕЗАНИЕ СИМВОЛОВ С КОНЦА СТРОКИ
print(greeting[-10:-3])
#ВЫРЕЗАЕТСЯ ВСЯ СТРОКА
print(greeting[2:])
#ВЫРЕЗАЕТСЯ ДО УКАЗАННОГО ИНДЕКСА
print(greeting[:7])
#ВЫРЕЗАЕТСЯ ВСЯ СТРОКА
print(greeting[:])

#ШАГ КОПИРОВАНИЯ
#ПЕРЕСКАКИВАЕМ ЧЕРЕЗ ОДИН СИМВОЛ
print(greeting[::2])
#ШАГ [1] ВЫВОДИТСЯ ВСЁ ПО ПОРЯДКУ
print(greeting[::1])
#ШАГ[3] БУДЕТ ВЫВОДИТЬСЯ КАЖДЫЙ ТРЕТИЙ СИМВОЛ
print(greeting[::3])
#МОЖЕМ УКАЗАТЬ С КАКОГО СИМВОЛА ВЫВОДИТЬ ШАГ
print(greeting[2::2])
#УКАЗЫВАЕМ ПЕРВЫЙ И ПОСЛЕДНИЙ СИМВОЛЫ, И ШАГ
print(greeting[0:9:2])
#ПЕРЕВОРАЧИВАНИЕ СТРОКИ,ВЫВОД СИМВОЛОВ В ОБРАТНОМ ПОРЯДКЕ
print(greeting[::-1])

#Домашнее задание
#Задача №1
string_1 = "Hello Python!"
print(string_1[3])

#ЗАДАЧА №2
print('Hello Python!'[3])

#ЗАДАЧА №3
string_2 = "Hello Python"
print(string_2[0:2])
print(string_2[0:-10])

#ЗАДАЧА №4
string_3 = 'Hello Python!'
path = string_3[6] + 'a' + string_3[8:10]
print(path)
string_4 = 'Pososi Pidor'
sosiskapi = string_4[2:6] + 'ska' + string_4[7:9]
print(sosiskapi)