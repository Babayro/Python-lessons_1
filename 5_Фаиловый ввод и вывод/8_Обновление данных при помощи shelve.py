xvgbgkbm = 'ОБНОВЛЕНИЕ ДАННЫХ ПРИ ПОМОЩИ МОДУЛЯ shelve'
import shelve
# ОБНОВЛЕНИЕ ДАННЫХ ПРИ ПОМОЩИ МОДУЛЯ shelve НА ПРИМЕРЕ РАСПИСАНИЯ
monday_schedule = ['Math', 'English Language', 'System programing', 'Python']
tuesday_schedule = ['English Language', 'HTML', 'Python', 'Football']
wednesday_schedule = ['Physics', 'English Language', 'Python']
thursday_schedule = ['Math', 'Chemistry', 'Java']
friday_schedule = ['Runing', 'Math', 'Python']

with shelve.open('schhedules', writeback=True) as schedules:
    schedules['monday_schedule'] = monday_schedule
    schedules['tuesday_schedule'] = tuesday_schedule
    schedules['wednesday_schedule'] = wednesday_schedule
    schedules['thursday_schedule'] = thursday_schedule
    schedules['friday_schedule'] = friday_schedule
# ПОЛУЧАЕМ ФАЙЛ БАЗЫ ДАННЫХ СО СПИСКАМИ С РАСПИСАНИЕМ ПО ДНЯМ НЕДЕЛИ

# ЕСЛИ МЫ ДОБАВИМ НОВЫЙ ОБЪЕКТ В СПИСОК, ТО НИЧЕГО НЕ ИЗМЕНИТСЯ Т.К. НОВЫЙ ОБЪЕКТ ОТОБРАЗИТСЯ В ПАМЯТИ А НЕ В ФАЙЛЕ
# ЭТО СДЕЛАННО ДЛЯ ТОГО, ЧТОБЫ НЕ ЗАСОРЯТЬ БАЗУ ДАННЫХ
# schedules['thursday_schedule'].append('Swiming')

# ПЕРВЫЙ СПОСОБ
# СОЗДАЁМ ВРЕМЕННЫЙ СПИСОК В НЕГО ЗАПИСЫВАЕМ СПИСОК thusday_schedule, И ЗАПИСЫВАЕМ ТУДА Swiming, ЗАТЕМ  ВРЕМЕННЫЙ СПИСОК ЗАПИСЫВАЕМ В СПИСОК
# В КОТОРОМ МЫ ДЕЛАЕМ ИЗМЕНЕНИЯ
    temp_list = schedules['thursday_schedule']
    temp_list.append('Swimming')
    schedules['thursday_schedule'] = temp_list
# ВТОРОЙ СПОСОБ ОБНОВЛЕНИЯ, В ВЕРХУ ВНОСИМ ИЗМЕНЕНИЯ ПРИ ОТКРЫТИЕ ФАИЛА with shelve.open('schhedules', writeback=True)
# ДАННЫЙ ТСПОСОБ ПОДХОДИ ДЛЯ НЕБОЛЬШИХ ОБНОВЛЕНИЙ, ИНАЧЕ ОН МОЖЕТ ВЫЗВАТЬ ПЕРЕГРУЗКУ ПРОЦЕССОРА, ЛУЧШЕ ПОЛЬЗОВАТЬСЯ ПЕРВЫМ СПОСОБОМ

    schedules['thursday_schedule'].append('Box')
    for key in schedules:
        print(key, schedules[key])
# pickle и shelve НЕ БЕЗОПАСНЫ С ТОЧКИ ЗРЕНИЯ ВИРУСОВ, ЕСЛИ ИХ ИСПОЛЬЗОВАТЬ С НЕИЗВЕСТНЫМ ИСТОЧНИКОМ
# ТАКЖЕ ФАЙЛ С ОБЪЕКТАМИ МОЖЕТ БЫТЬ ПОВРЕЖДЁН КОГДА К НЕМУ ОДНОВРЕМЕННО ОБРАЩАЮТСЯ ИЗ РАЗНЫХ ИСТОЧНИКОВ




