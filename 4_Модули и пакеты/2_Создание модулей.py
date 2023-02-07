print('СОЗДАНИЕ МОДУЛЕЙ, РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')
# ПЕРВЫЙ СПОСОБ ИМПОРТА
from greetings import say_hello
from greetings import say_hi
say_hello()
say_hi()


# ВТОРОЙ СПОСОБ ИМПОРТА
import goodbyes

goodbyes.say_hasta_la_vista()
goodbyes.say_bye_bye()

# ИМПОРТ ОДНОЙ ФУНКЦИИ ИЗ МОДУЛЯ, БЕЗ ВЫЗОВА ВСЕГО МОДУЛЯ

from greetings import say_hey_there
say_hey_there()


