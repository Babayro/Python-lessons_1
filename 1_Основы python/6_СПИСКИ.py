#3. ВЫВОД СПИСКА С ПРОСТЫМИ ЧИСЛАМИ
lesson = 'СПИСКИ(LISTS) РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ:'
print(lesson)
number_list = [32, 21, 48]
print(number_list)

# ВЫВОД СПИСКА С ОБЪЕКТАМИ РАЗНОГО ТИПА ДАННЫХ
# САМИ СПИСКИ ТАКЖЕ ЯВЛЯЮТСЯ ОБЪЕКТАМИ
some_list = [12, 3.6, 'Hellou']
print(some_list)

# ФУНКЦИЯ "len" ВЫВОДИТ КОЛИЧЕСТВО ЭЛЕМЕНТОВ СПИСКА
print(len(some_list))

# ВЫВОД ПЕРВОГО ЭЛЕМЕНТА СПИСКА
print(some_list[1])

# ВЫРЕЗАНИЕ ЭЛЕМЕНТОВ СПИСКА (ОТСЧЁТ С 0 И ДО КОТОРОГО ВЫРЕЗАЕМ)
another_list = some_list[:2]
print(another_list)

# В СТРОКАХ НЕЛЬЗЯ В СТРОКАХ МЕНЯТЬ СИМВОЛЫ, ИХ МОЖНО ТОЛЬКО ВЫРЕЗАТЬ И ПЕРЕНОСИТЬ В НОВУЮ СТРОКУ.
# В СПИСКАХ МОЖНО МЕНЯТЬ ОБЪЕКТЫ.
some_list[2] = 'hi'
print(some_list)

# КОНКАТЕНАЦИЯ СПИСКОВ
new_list = another_list + some_list
print(new_list)

# ПРИСВОЕНИЕ СПИСКУ НОВОГО ЭЛЕМЕНТА ПРИ ПОМОЩИ МЕТОДА append (ОН ДОБАВЛЯЕТ НОВЫЙ ЭЛЕМЕНТ В КОНЕЦ СПИСКА)
new_list.append('NEW ITEM')
print(new_list)

# ДОБАВЛЯЕМ ЭЛЕМЕНТ В НАЧАЛО СПИСКА ПРИ ПОМОЩИ МЕТОДА insert (ВСТАВИТЬ)
# В ЭТОМ МЕТОДЕ МЫ МОЖЕМ  УКАЗАТЬ КУДА МЫ ХОТИМ ВСТАВИТЬ
new_list.insert(0, 'start')
print(new_list)

# ЕСЛИ МЫ ХОТИМ ВСТАВИТЬ В ЛЮБОЕ ДРУГОЕ МЕСТО, ТО ПРОСТО ВЫВОДИМ ПОРЯДКОВЫЙ НОМЕР ОТ 0 И НОМЕР ОБЪЕКТЫ ДО
# ЗАТЕМ САМ ОБЪЕКТ КОТОРЫЙ ХОТИМ ВСТАВИТЬ
new_list.insert(2, 'start')
print(new_list)

# УДАЛЕНИЕ ЭЛЕМЕНТОВ (ROMOVING ITEMS)
# УДАЛЕНИЕ ПОСЛЕДНЕГО ЭЛЕМЕНТА ПРИ ПОМОЩИ МЕТОДА pop
new_list.pop()
print(new_list)

# ПРИ УКАЗАНИИ ПОСЛЕДНЕГО ЭЛЕМЕНТА ТАКЖЕ УДАЛИТЬСЯ ПОСЛЕДНИЙ ЭЛЕМЕНТ
new_list.pop(-1)
print(new_list)

#УДАЛЕНИЕ ПЕРВОГО ЭЛЕМЕНТА
new_list.pop(0)
print(new_list)

# УДАЛЕНИЕ ЭЛЕМЕНТА ИЗ СЕРЕДИНЫ "start" ОТСЧЁТ ОТ -1 ПО САМ ЭЛЕМЕНТ ВКЛЮЧИТЕЛЬНО
new_list.pop(-4)
print(new_list)

# УДАЛЕНИЕ И ВОЗВРАЩЕНИЕ ЭЛЕМЕНТА
delite_item = new_list.pop(0)
print(new_list)
print(delite_item)

# МЕТОД romove (ЭТОТ МЕТОД НЕ ВОЗВРАЩАЕТ ЗНАЧЕНИЯ) УДАЛЯЕТ НЕ ПО ИНДЕКСУ, А ПО ЗНАЧЕНИЮ
# ЕСЛИ В СПИСКЕ ЕСТЬ ОДИНАКОВЫЕ ЗНАЧЕНИЯ, ТО ОН УДАЛЯЕТ ПЕРВОЕ ПО СЧЁТУ
# МЫ ПОЛУЧАЕМ НОВЫЙ СПИСОК БЕЗ УДАЛЁННОГО ЭЛЕМЕНТА
print(new_list)
delite_new_list = new_list.remove(3.6)
print(new_list)
print(delite_new_list)

# СОРТИРОВКА ЭЛЕМЕНТОВ СПИСКОВ ПРИ ПОМОЩИ МЕТОДА sort(НЕ ВОЗВРАЩЫЕТ ЗНАЧЕНИЙ)
# СОРТИРУЕТ ПО ПОРЯДКУ: ОТ МЕНЬШЕГО К БОЛЬШЕМУ И ПО АЛФАВИТУ
number_list = [42, -35, 22, 78, 94]
letter_list = ['a', 'b', 'c', 'f', 'h']
number_list.sort()
letter_list.sort()
print(number_list)
print(letter_list)

#СОХРАНЕНИЕ ОТСОРТРОВАННОГО СПИСКА В НОВОЙ ПЕРЕМЕННОЙ
letter_list.sort()
saved_letter_list = letter_list
print(saved_letter_list)

# МЕТОД reverse ВЫСТРАИВАЕТ ЭЛЕМЕНТЫ В ОБРАТНОМ ПОРЯДКЕ
number_list.reverse()
letter_list.reverse()
print(number_list)
print(letter_list)

# СПИСКИ МОЖНО ДОБАВЛЯТЬ ДРУГ В ДРУГА ПРИ ПОМОЩИ МЕТОДА append
number_list.append(letter_list)
print(number_list)

# ДОМАШНЕЕ ЗАДАНИЕ
new_data_list = [15, 35, -24, 'hi',1.23]
carved_new_data_list = new_data_list [:3]
print(carved_new_data_list)