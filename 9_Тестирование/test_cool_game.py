import unittest
import cool_game
# TDD СНАЧАЛО ПИШЕМ ТЕСТЫ, А ПОТОМ СОЗДАЁМ НУЖНЫЕ НАМ ФУНКЦИИ ИЛИ КЛАССЫ
class CoolGameFunctionsTest(unittest.TestCase): # СОЗДАЁМ КЛАССИ НАСЛЕДУЕМСЯ ОТ КЛАССА В СКОБКАХ
    # ПЕРВЫЙ ТЕСТ, ВСТРЕЧАЕМ ДРУГА
    """
    Также можем описывать работу функций в тех.документации
    """
    def test_greet(self): # СОЗДАЁМ ТЕСТ ДЛЯ ФУНКЦИИ greet
        self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?') # МЕТОД КОТОРЫЙ УТВЕРЖДАЕТ РАВЕНСТВО
        # ДВУХ ПАРАМЕТРОВ КОТОРЫЕ МЫ В НЕГО ПЕРЕДАДИМ

    # ВТОРОЙ ТЕСТ, БУДЕМ ВСТРЕЧАТЬ ВРАГА
    def test_greet_is_enemy(self): # СОЗДАЁМ ТЕСТ ДЛЯ ФУНКЦИИ greet
        self.assertEqual(cool_game.greet('Sipa', True), 'Hello Sipa! I will kill you, bastard!')

    # ТЕСТ ДЛЯ ФУНКЦИИ eat_burgers
    def test_eat_burgers(self):
        self.assertEqual(cool_game.eat_burgers(3), 'Mmm! That was exellent!')

    def test_eat_too_much_burgers(self):
        self.assertEqual(cool_game.eat_burgers(4), 'Oh! I overate!')

    def test_can_fly(self):
        self.assertTrue(cool_game.can_fly('Batman'), 'Batman have to be able to fly')
    # ЕСЛИ МЫ ПЕРЕДАЁМ ЛЮБОЕ ИМЯКРОМЕ БЭТМЕНА, ТО УКАЗЫВАЕМ, ЧТО ЭТОТ ПЕРСОНАЖ НЕ ДОЛЖЕН УМЕТЬ ЛЕТАТЬ
    def test_can_fly_anyone_else(self):
        self.assertEqual(cool_game.can_fly('Bob'), False)
        self.assertEqual(cool_game.can_fly('Jim'), False)
        self.assertEqual(cool_game.can_fly('Sipa'), False)


    def test_get_arsenal(self):
        self.assertIn(cool_game.get_arsenal(),('knife', 'handgun', 'machine gun')) # УТВЕРЖДАЕМ, ЧТО ДОЛЖЕН БЫТЬ КОРТЕЖ


if __name__ == "__main__":
    unittest.main()