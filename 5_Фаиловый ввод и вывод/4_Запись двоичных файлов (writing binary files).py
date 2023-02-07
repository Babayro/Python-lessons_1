ytt = 'ЗАПИСЬ ДВОИЧНЫХ ФАЙЛОВ (WRITING BINARY FILES, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(ytt)

# ЦЕЛЫЕ ЧИСЛА И СТРОКИ ДОЛЖНЫ БЫТЬ ПРИВЕДЕНЫ В СПЕЦИАЛЬНЫЙ ФОРМАТ БАЙТЦ, А ТОЛЬКО ПОТОМ В ДВОИЧНЫЙ КОД
# НУЖНО ОБЯЗАТЕЛЬНО УКАЗАТЬ БУКВУ b = бинарный текстовый файл, а не обычный текстовый файл
with open('test_binary', 'bw') as test_file:
    for number in range(21):
        test_file.write(bytes([number]))
# ОТКРЫВАЕМ ФАИЛ ЧТОБЫ ПРОЧИТАТЬ ЕГО
with open('test_binary', 'br') as test_file:
    for number in test_file:
        print(number)