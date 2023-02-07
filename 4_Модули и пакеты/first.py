# ФУНКЦИЯ __name__ and '__main__'
print(1)
print('string')

# ЕСЛИ ФАИЛ САПУСКАЕТСЯ БЕЗ ИМПОРТА ТО ПЕРЕМЕННАЯ __name__ ПРИНИМАЕТ ЗНАЕНИЕ main
__name__ = '__main__'
print(__name__)

def function1():
    pass

def function_2():
    pass

class MyClass:
    pass
# МЫ ПРОВЕРЯЕМ ДЕЙСТВИТЕЛЬНОЛИ ЭТИ ФУНКЦИИ НЕ ИМПОРТИРОВАННЫ, А ЗАПУСКАЮТСЯ В ФАИЛЕ ПАПРЯМУЮ, И ПОТОМ УЖЕ ИХ ИСПОЛНЯЕМ
if __name__== '__main__':
    function1()
    function_2()

def function_1():
    print('function_1() from first.py')


def function_2():
    print('function_2() from first.py')


if __name__ == '__main__':
    function_1()