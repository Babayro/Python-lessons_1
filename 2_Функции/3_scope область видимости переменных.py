scope = 'Scope ОБЛАСТЬ ВИДИМОСТИ ПЕРЕМЕННЫХ РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'

pi = 'outer pi variable'


def print_pi():
    pi = 'inner pi variable'
    # ОБРАЩАЕТСЯ К ЛОКАЛЬНОЙ ПЕРЕМЕННОЙ
    print(pi)

print_pi()
# С НАРУЖИ ОБРАЩАЕТСЯ К ГЛОБАЛЬНОЙ ПЕРЕМЕННОЙ
print(pi)

# Local Scope
pi = 'global pi variable'
def inner():
    pi = 'inner pi variable'
    print(pi)


# Local Scope
pi = 'global pi variable'
def inner():
    # pi = 'inner pi variable'
    print(pi)


# Enclosed Scope
pi = 'global pi variable'
def outer():
    pi = 'outer pi variable'

    def inner():
        nonlocal pi
        pi = 'inner pi variable'
        # nonlocal pi
        print(pi)

    inner()


outer()
print(pi)


