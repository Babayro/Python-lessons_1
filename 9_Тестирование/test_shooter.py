# МЕТОДЫ setUP ВОСТАНОВИТЬ ОН ЗАПУСКАЕТСЯ ДО КАЖДОГО ТЕСТОВОГО МЕТОДА
# ЕСЛИ МЫ ХОТИМ ЗАФИКСИРОВАТЬ НАШЕ ПРИЛОЖЕНИЕ В КАКОМ-ТО СОСТОЯНИИ И НАЧАЛИ ТЕСТИРОВАТЬ ЕГО В ЭТОМ СОСТОЯНИИ
# ИСПОЛЬЗУЕМ ЭТОТ МЕТОД

# tearDown УНИЧТОЖИТЬ ЗАПУСКАЕТСЯ ПОСЛЕ КАЖДОГО ТЕСТОВОГО МЕТОДА
# ОНИ НУЖНЫ КОГДА МЫ ТЕСТИРУЕМ ПРИЛОЖЕНИЕ И ИСПОЛЬЗУЕМ ЛОЖНЫЕ ДАННЫЕ
# ЧТОБЫ УДАЛИТЬ ЛОЖНЫЕ ТЕСТОВЫЕ ДАННЫЕ ИСПОЛЬЗУЕМ ЭТОТ МЕТОД

import unittest
from shooter import Shooter


class ShooterTest(unittest.TestCase):# НАСЛЕДУЕМСЯ ОТ КЛАССА В СКОБКАХ

	mock_data = [] # ПУСТОЙ СПИСОК!

	def setUp(self):
		self.jake = Shooter('Jake') #НАМ НЕ НУЖНО В КАЖДОМ ТЕСТЕ СОЗДАВАТЬ НОВЫЙ ОБЪЕКТ БЛАГОДАРЯ setUp
        # ОН БУДЕТ СОЗДАВАТЬСЯ АВТОМАТИЧЕСКИ ПЕРЕД ВЫЗОВОМ КАЖДОГО ТЕСТОВОГО МЕТОДА
		print(self.mock_data) # ПУСТОЙ СПИСОК!
		self.mock_data = [1, 2, 3, 4, 5]# ПОЛНЫЙ СПИСОК! #НАМ НЕ НУЖНО В КАЖДОМ ТЕСТЕ СОЗДАВАТЬ НОВЫЙ ОБЪЕКТ БЛАГОДАРЯ setUp

	def tearDown(self):
		print(self.mock_data) # ЕЩЁ ПОЛНЫЙ СПИСОК
		self.mock_data = [] # ПУСТОЙ СПИСОК!#БУДЕТ ОЧИЩАТЬ СПИСОК КОТОРЫЙ ВЫШЕ ПОСЛЕ РАБОТЫ КАЖДОГО ТЕСТОВОГО МЕТОДА

	def test_get_cash(self):
		# jake = Shooter('Jake')НАМ НЕ НУЖНО В КАЖДОМ ТЕСТЕ СОЗДАВАТЬ НОВЫЙ ОБЪЕКТ БЛАГОДАРЯ setUp
		self.jake.get_cash(500)
		self.assertEqual(self.jake.money, 1500)
		print(self.mock_data) # В ЭТОМ ТЕСТЕ ДАННЫЕ ОПЯТЬ ДОБАВЛЯЮТСЯ В СПИСОК

	def test_greet(self):
		# jake = Shooter('Jake')НАМ НЕ НУЖНО В КАЖДОМ ТЕСТЕ СОЗДАВАТЬ НОВЫЙ ОБЪЕКТ БЛАГОДАРЯ setUp
		self.assertEqual(self.jake.greet(), 'Hello! How are you?')
		self.jake.money = 50
		self.assertEqual(self.jake.greet(), 'Hello! I need cash!')



if __name__ == '__main__':
	unittest.main()