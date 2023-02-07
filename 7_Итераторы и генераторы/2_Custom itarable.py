print('Custom iterable, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
# СОЗДАЁМ СВОИ СОБСТВЕННЫЕ ОБЪЕКТЫ iterable

# СОЗДАЁМ КЛАСС С ПАРАМЕТРАМИ ДИАПАЗОНА START И END, ДОБАВЛЯЕМ CURRENT ТЕКУЩЕЕ ЗНАЧЕНИЕ
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
# ВОЗВРАЩАЕМ ВЕРХНИЙ ОБЪЕКТ
    def __iter__(self):
        return self
# ДЕЛАЕМ ВЕРХНИЙ ОБЪЕКТ ИТЕРАТОРОМ ПРИ ПОМОЩИ ФУНКЦИИ NEXT
    def __next__(self):
# СОЗДАЁМ УСЛОВИЕ ВЫВОДА В ДИАПАЗОНЕ
        if self.current < self.end:
# В ПЕРЕМЕННУЮ number ЗАПИСЫВАЕМ СТАРТОВОЕ ЗНАЧЕНИЕ
            number = self.current
# ЕСЛИ УСЛОВИЕ ВЕРНО ТО УВЕЛИЧИВАЕМ current НА 1
            self.current += 1
# ВОЗВРАЩАЕМ ЗНАЧЕНИЕ В ПЕРЕМЕННУЮ number
            return number
# ДЛЯ ОСТАНОВКИ БЕСКОНЕЧНОГО ЦИКЛА, ПРИ ВЫПОЛНЕНИИ УСЛОВИЯ, ОСТАНАВЛИВАЕМ ЦИКЛ С ПОМОЩЬЮ ОШИБКИ
        raise StopIteration

# ЗАПУСКАЕМ ЦИКЛ ДЛЯ ВЫВОДА ЗНАЧЕНИЙ В ЗАДАННОМ ДИАПАЗОНЕ
first_range = MyRange(20, 30)
for number in first_range:
    print(number)

