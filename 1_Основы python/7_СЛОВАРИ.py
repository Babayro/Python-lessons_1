# 4.СЛОВАРИ СОДЕРЖАТ В СЕБЕ НЕУПОРЯДОЧЕННУЮ ПОСЛЕДОВАТЕЛЬНОСТЬ ОБЪЕКТОВ
# СЛОВАРИ СОСТОЯТ ИЗ КЛЮЧЕЙ И ЗНАЧЕНИЙ
# МАРКА МАШИНЫ ЭТО КЛЮЧ, А ЦЕНА ЭТО ЗНАЧЕНИЕ
cars_prices = {'opel': 5000, 'toyota': 7000, 'bmw':10000 }
print(cars_prices)
print(cars_prices['toyota'])

# ДОБАВЛЕНИЕ НОВОГО ЭЛЕМЕНТА
cars_prices ['mazda'] = 4000
print(cars_prices)

# ИЗМЕННЕНИЕ ЗНАЧЕНИЯ КЛЮЧА В СЛОВАРЕ
cars_prices['opel'] = 2000
print(cars_prices)

# УДАЛЕНИЕ ЗНАЧЕНИЯ ПРИ ПОМОЩИ КОМАНДЫ dell
# ОПАСНО!!! ЕСЛИ УКАЗАТЬ ПУСТЫЕ СКОБКИ БЕЗ КЛЮЧА УДАЛЕНИЯ, ТО УДАЛИТСЯ ВЕСЬ СЛОВАРЬ С ПЕРЕМЕННОЙ!!!
del cars_prices['toyota']
print(cars_prices)

# УДАЛЕНИЕ ОБЪЕКТОВ СЛОВАРЯ БЕЗ УДАЛЕНИЯ ПЕРЕМЕННЫХ ПРИ ПОМОЩИ МЕТОДА clear
cars_prices.clear()
print(cars_prices)

# СЛОВАРИ ВНУТРИ СЕБЯ МОГУТ СОДЕРЖАТЬ БОЛЕЕ СЛОЖНЫЕ СТРУКТУРЫ(ДРУГИЕ СЛОВАРИ ИЛИ СПИСКИ)
person = {
    'name': 'Simon',
    'last name': 'Simons',
     'Age': 23,
    'Hobbis': ['sex', 'drags', 'porno', 'algkohol'],
     'children': {'doter': 'Abba', 'son':'Pira'}
}
# ВЫВОД КОНКРЕТНОГО ЭЛЕМЕНТА
print(person['Age'])
print(person['Hobbis'])
# СОЗДАЁМ НОВУЮ ПЕРЕМЕННУЮ В НЕЁ  ЗАПИСЫВАЕМ СЛОВАРЬ person И СПИСОК 'Hobbis'
hobbis = person ['Hobbis']
# ВЫВОДИМ НОВУЮ ПЕРЕМЕННУЮ КОТОРАЯ СОДЕРЖИТ В СЕБЕ СПИСОК 'Hobbis' И ВЫВОДИМ ИНДЕКС ЭЛЕМЕНТА [2]
print(hobbis[1])
children = person ['children']
print(children['son'])
print(children['doter'])
print(children['son'])
# ДОБАВЛЕНИЕ ОБЪЕКТА В СЛОВАРЬ
# СЛОВАРЮ ПРИСВАИВАЕМ КЛЮЧ СО ЗНАЧЕНИЕМ
person['car'] = 'Mazda'
print(person)
# ИЗМЕНЕНИЕ ЗНАЧЕНИЙ
person['Hobbis'][0]='Footbool'
print(person)
# МЕТОД ПОЛУЧЕНИЯ ВСЕХ КЛЮЧЕЙ keys
print(person.keys())
# МЕТОД ПОЛУЧЕНИЯ ДОСТУПА КО ВСЕМ ЗНАЧЕНИЯМ values
print(person.values())
# МЕТОД ПОЛУЧЕНИЯ ВСЕХ ЭЛЕМЕНТОВ items
print(person.items())