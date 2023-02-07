# Тема 2 Строки.
string_tema = '"ТEMA 2 СТРОКИ РЕЗУЛЬТАТ"'
print(string_tema)
greeting = "Hello"
print(greeting)
# Сложение строк при помощи арифметического оператора "+"
first_name = "Ivan"
last_name = "Gridin"
znak = "!"
probel = " "
print(greeting + probel + first_name + " " + last_name + znak)

# Вывод "'" после "\"
some_string = 'I\'am a Python programmer'
print(some_string)

# Вывод двойных ковычек при помощи "\" = \"Python\"
some_string_2 = "i wont to learn \"Python\""
print(some_string_2)

# "\n" перенос строки в низ, в начале нижней строки будет пробел.
string_with_new_line = "Hellou! \n Myname is Yura"
print(string_with_new_line)

# Возврат каретки: если после "n"" мы укажем пробелы, то выведется пробелов сколько мы указали.
# Если мы поставим "\r" то произойдет возврат каретки после переноса строки
# При этом количество пробелов \n между\r не влияет на отображение строки.
string_with_new_line = "Hello! \n \rMyname is Yura"
print(string_with_new_line)

# Если мы уберём пробел \n между Myname is Yura" то также произойдёт возврат каретки
string_with_new_line = "Hello! \nMyname is Yura"
print(string_with_new_line)

# Если добавляем "\t" то по "1" появляется несколько пробелов
numbers = "1\t234567"
print(numbers)

# Табуляция после "t"
numbers = "1\t234\t56\t7"
print(numbers)

# Абзац "\t" и перенос строки после "\n"
some_text = "\tHellou!\nI see you"
print(some_text)

# Абзац "\t" и перенос строки после "\n", \r табуляция, выравнивание по обзацам
some_text = "\tHellou!\n\tI see you"
print(some_text)

# Triple quotes (тройные кавычки)  внутри можно размещать как двойные, так и одинарные кавычки
triple_quotes = """ This' is text with "triple quotes" """
print(triple_quotes)

# Тройные одинарные кавычки работают так же как и обычные тройные кавычки.
triple_quotes_2 = ''' This' is text with "triple quotes" '''
print(triple_quotes_2)

# Перенос строки с сохранением выравнивания с помощью тройных кавычек (не нужен "\n")
triple_quotes_3 = ''' This' is text with 
"triple quotes" '''
print(triple_quotes_3)