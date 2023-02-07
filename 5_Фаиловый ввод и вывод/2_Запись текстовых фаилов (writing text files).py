sdeff = 'ЗАПИСЬ ТЕКСТОВЫХ ФАИЛОВ (writing text files), РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(sdeff)
# МОЖЕМ ДОБАВЛЯТЬ НОВЫЕ ЗНАЧЕНИЯ В ФАИЛ, МОЖЕМ СОЗДАТЬ НОВЫЙ ФАИЛ С ТЕМЕЖЕ ЗНАЧЕНИЯМИ ПРОСТО ИЗМЕНИВ НАЗВАНИЕ ФАИЛА
colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
with open('/home/silistin/Рабочий стол/raibow_colors.txt', 'w') as raibow_colors:# 'w' = ЗАПИСЬ
    for color in colors_list:
        print(color, file=raibow_colors)

                                      # СЧИТЫВАЕМ СОЗДАННЫЙ ФАИЛ
colors_list = []
with open('/home/silistin/Рабочий стол/raibow_colors.txt', 'r') as raibow_colors:# 'r' = ЧТЕНИЕ
    for color in raibow_colors:
        colors_list.append(color.strip('\n'))# МЕТОД strip ОБРЕЗАЕТ '\n'
print(colors_list)

# ДОБАВЛЯЕМ, А НЕ ПЕРЕЗАПИСЫВАЕМ В ФАИЛ НОВЫЕ СТРОКИ ПРИ ПОМОЩИ МЕТОДА 'a'(append)
with open('/home/silistin/Рабочий стол/raibow_colors.txt', 'a') as raibow_colors:
    print('dark green',file=raibow_colors)
    print('dark blue', file=raibow_colors)