import unittest
import upper


class TestUpper(unittest.TestCase):# НАСЛЕДУЕМСЯ ОТ КЛАССА УКАЗАННОГО В СКОБКАХ
	"""docstring for ClassName"""
	def test_one_word(self): # АКТИВИРУЕМ МЕТОДЫ КЛАССА
		text = 'hello!'# ПЕРЕДАЁМ В НАШУ ФУНКЦИЮ ТАКТС ДЛЯ ПРОВЕРКИ
		result = upper.upper_text(text)# ПЕРЕДАЁМ НАШУ ИМПОРТИРУЕМУЮ ФУНКЦИЮ
		self.assertEqual(result, 'Hello!')# МЕТОД ПРОВЕРКИ СООТВЕТСТВИЯ УТВЕРЖДЕНИЮ
		self.assertNotEqual(result, 'hello!')# УТВЕРЖДЕНИЕ ЧТО ПАРАМЕТР НЕ ДОЛЖЕН БЫТЬ РАВЕН УКАЗАННОМУ


	def test_multiple_words(self):
		text = 'hello world!'
		result = upper.upper_text(text)
		self.assertEqual(result, 'Hello World!')


if __name__ == '__main__':
    unittest.main()