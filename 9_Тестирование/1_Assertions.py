print('ASSERTIONS РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ')

# assertions - УТВЕРЖДЕНИЕ
assert 2 + 2 == 4
# assert 2 + 2 == 5 '2 + 2 должно быть равно 4'


def multiply_positive_numbers(a, b):
    assert a > 0 and b > 0, 'a and b must be positive'
    print (a * b)

multiply_positive_numbers(3, 5)

def get_access(password):
    password_list = [111, 222, 333]
    assert int(password) in password_list, 'Password is invalid'
    print('You can make dangerous stuff')

password_1 = input('Please input the password')
get_access(password_1)

# ASSERT НЕ РАБОТАЕТ В ОПТИМИЗИРОВАННОМ РЕЖИМЕ!!!