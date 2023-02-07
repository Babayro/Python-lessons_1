print('КОНВЕРТАЦИЯ СЛОВАРЯ В ОБЪЕКТ shelve, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')

# 2. СОЗДАЁМ ОБЪЕКТ shelve
import shelve
# 1. СЛОВАРЬ ПО КЛЮЧУ schedules
university = {
    "schedules": {
        'monday_schedule' : ['Math', 'English Language', 'System programing', 'Python'],
        'tuesday_schedule' : ['English Language', 'HTML', 'Python', 'Football'],
        'wednesday_schedule' : ['Physics', 'English Language', 'Python'],
        'thursday_schedule' : ['Math', 'Chemistry', 'Java'],
        'friday_schedule' : ['Runing', 'Math', 'Python']
    },
# ДОБАВЛЯЕМ В ПЕРМЕННУЮ university СЛОВАРЬ tutors
    'tutors': {
        'Math': ['Jack White', 'Jim Black'],
        'Python': ['YouRa Allakherdov', 'Jane Smith']
    }
}
print(university['schedules']['wednesday_schedule'])
print(university ['tutors']['Math'])

# 2. СОЗДАЁМ ОБЪЕКТ shelve
print('СОЗДАЁМ ОБЪЕКТ shelve')
import shelve

university = shelve.open('university_file')
university['schedules'] = {

        'monday_schedule' : ['Math', 'English Language', 'System programing', 'Python'],
        'tuesday_schedule' : ['English Language', 'HTML', 'Python', 'Football'],
        'wednesday_schedule' : ['Physics', 'English Language', 'Python'],
        'thursday_schedule' : ['Math', 'Chemistry', 'Java'],
        'friday_schedule' : ['Runing', 'Math', 'Python']
    }
# ДОБАВЛЯЕМ В ПЕРМЕННУЮ university СЛОВАРЬ tutors
university['tutors'] = {
        'Math': ['Jack White', 'Jim Black'],
        'Python': ['YouRa Allakherdov', 'Jane Smith']
    }
print(university['schedules']['wednesday_schedule'])
print(university ['tutors']['Math'])
# ПОСЛЕ ВСЕХ МАНИПУЛЯЦИЙ ЗАКРЫВАЕМ СОЗДАННЫЙ ОБЪЕКТ
university.close()