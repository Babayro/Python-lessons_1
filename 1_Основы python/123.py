def count_up_to(x):
    count = 1
 # ПОКА  count МЕНЬШЕ ИЛИ РАВНО ИКС МЫ УВЕЛИЧИВАЕМ ЕГО ЗНАЧЕНИЕ ПОСРЕДСТВОМ ИТЕРАЦИЙ С 1 И ДО УКАЗАННОГО НАМИ ПРИ ВЫЗОВЕ ФУНКЦИИ
    while count <= x:
# ФУНКЦИЯ yield ВЫРАБАТЫВАЕТ ЗНАЧЕНИЯ И НЕ ОБНУЛЯЕТСЯ ПОСЛЕ ИТЕРАЦИИ, ТАКЖЕ КАК И next ЗАСЫПАЕТ ПОСЛЕ ПЕРВОЙ И ПОСЛЕДУЮЩИХ ИТЕРАЦИЙ
# ПРИ ЗАСЫПАНИИ ОНА ЗАПОМИНАЕТ ПОСЛЕДНЕЕ ЗНАЧЕНИЕ, И ДАЛЕЕ РАБОТА БУДЕТ НАЧАТА НЕ С 0, А С ЗАПОМНИННОГО СОСТОЯНИЯ
        yield count
        count += 1











































































