dkfvtk = 'МОДУЛЬ PICKLE, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
print(dkfvtk)
# ДАННЫЙ МОДУЛЬ КАКБЫ КОНСЕРВИРУЕТ ОБЪЕКТ (СОХРАНЯЕТ ЕГО В ДВОИЧНОМ ФАИЛЕ, ПАМЯТИ КОМПЬЮТЕРА), ЧТОБ В СЛУЧАЕ НЕОБХОДИМОСТИ МЫ МОГЛИ ВОСТАНОВИТЬ ВСЕ ДАННЫЕ ОБЪЕКТА
import pickle

honda = (
    'civic',
    'grey',
    '2009',
    (
        (1, 'James Brown'),
        (2, 'jane White'),
        (3, 'Jake Green'),
    )
)
# СОХРАНЯЕМ ДАННЫЙ ОБЪЕКТ В ДВОИЧНОМ ФАЙЛЕ
with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)

# МЕТОД LOAD ДЛЯ ИЗВЛЕЧЕНИЯ ОБЪЕКТА СОХРАНЁННОГО В ДВОИЧНОМ КОДЕ
with open('honda.pickle', 'rb') as honda_retrieved:
    honda_from_file = pickle.load(honda_retrieved)

print(honda_from_file)

model, color, year, owner_list = honda_from_file
print(model)
print(color)
print(year)
for owner in owner_list:
    owner_number, owner_name = owner
    print(owner_number, owner_name)

models = ['civic', 'accord', 'pilot']
owners = ['James Brown', 'Jane White', 'Jake Green']

# ВТОРОЙ СПОСОБО ЗАПИСИ И ИЗВЛИЧЕНИЯ (ПОРЯДОК ЗАПИСИ И ИЗВЛИЧЕНИЯ ВАЖЕН, ДОЛЖЕН СОВПАДАТЬ!!!)
with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)
    pickle.dump(models, honda_file)
    pickle.dump(owners, honda_file)
    pickle.dump(99999999999, honda_file)

with  open('honda.pickle', 'rb') as honda_retrieved:
    honda_from_file = pickle.load(honda_retrieved)
    models = pickle.load(honda_retrieved)
    owners = pickle.load(honda_retrieved)
    a = pickle.load(honda_retrieved)

print(honda_from_file)
print(models)
print(owners)
print(a)