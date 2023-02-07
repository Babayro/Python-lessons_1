x = 'ВЛОЖЕННЫЕ ЦИКЛЫ, ВЫПОЛНЕНИЕ ПРОГРАММЫ:'
print(x)
for number in range(10): # Внешний цикл (ВЕРТИКАЛЬ)
    count = 0
    smile = ''  # НЕ ОБНУЛЯЕТСЯ, А ПРИБАВЛЯЕТСЯ НОВЫЙ ПРИ КАЖДОЙ ИТЕРАЦИИ
    while count <= number: # count and number = 0 (ГОРИЗОНТАЛЬ)
        smile += '\U0001F600' # Присваивается значение и смайлик строке
        count += 1 # Прибавляеи +1 к count и проверяем условие в while, count = 1, а number 0, выполняем print, при следущей итерации count 1, number 1
    print(smile)# выход из циклв while

for number in range(10): # Внешний цикл (ВЕРТИКАЛЬ)
    smile = ''
    for count in range(number + 1):#(ГОРИЗОНТАЛЬ)
        smile += '\U0001F600'
    print(smile)
# ГОРИЗОТАЛЬ УМНОЖАЕМ НА ВЕРТИКАЛЬ (1 НОМЕР ИТЕРАЦИИ*1 СМАЙЛИК, 2 НОМЕР ИТЕРАЦИИ *1 СМАЙЛИК, 3*1 СМАЙЛИК...), ГОРИЗОНТАЛЬ НЕ ОБНУЛЯЕТСЯ
for number in range(1, 11):
    print('\U0001F600' * number) # Умножение строк

count = 1
while count <= 11: #  ПОКА ЕСТЬ УСЛОВИЕ, ГОРИЗОНТАЛЬ УМНОЖАЕМ НА ВЕРТИКАЛЬ
    print('\U0001F600' * count)
    count += 1

while True:
    name = input('Enter name')
    if name =='Pidor':
     continue # При выводе имени пидор, не выводит 'Hello!', а снова просит ввести имя
    print('Hello!', name)

while True:
    name = input("Введите имя:")
    if name == "хватит":
        break      # полностью выходит из цикла при вводе имени "хватит"
print("Привет", name)

num = 3 # Бесконечный цикл
while num < 5:
    print('Hello!')

d = [[1,2,3],[4,5,6]]
for i in range(2): # Вывод два раза
    for j in range(3): # Вывод 3-х объектов
        print(d[i][j])# d РАСКРЫВАЕМ СПИСОК, i ВЫВОДИТ ПЕРВЫЕ  И ПОСЛЕДУЮЩИЕ ДВА ЧИСЛА, j ВЫВОДИТ ТРИ РАЗА i


