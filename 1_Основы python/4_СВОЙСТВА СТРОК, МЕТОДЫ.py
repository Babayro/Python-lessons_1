#2.2.СВОЙСТВА СТРОК. МЕТОДЫ
name_lesson = '4.СВОЙСТВА СТРОК, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ:'
print(name_lesson)
#1-е Свойство: immutable = строки являются не изменяемые
#Строки-это упорядоченный набор символов
#Замена буквы "k" на "n"
first_name = 'Jake'
#print(first_name[2])
#first_name = [2] = +'n'
#print(first_name) будет ошибка!!!
first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)
#Конкатенация
new_first_name = first_two_letters + "n" + last_letter
print(new_first_name)

#Конкотенация
greeting = "Hello"
greeting = greeting + ' ' + "Python"
print(greeting)

#2-е Свойство Multipliсation (умножение строк)
yummi = "Yum "
print(yummi *2 )
#Методы строк
#Строки в данном языке являются объектом, а объекты имеют методы для работы
#Для вызова метода используем точку после переменной
#Методами создаются новые строки
print(yummi.upper())
print(yummi.lower())
#Старая строка не меняется
print(yummi)
#Разделяет на пять слов по пробелам
long_string = "This is the long string"
print(long_string.split())

#Домашнее задание
string_1 = 'HELLO Python'
string_p = string_1[6:7]
print(string_p)
string_ph = string_1[8:10]
print(string_ph)
new_string_1 = string_p + "a" + string_ph
print(new_string_1)

string_z = "z"
print(string_z * 7)
print(string_z.upper() *7)