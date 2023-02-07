# МЕТОДЫ setUP ВОСТАНОВИТЬ ОН ЗАПУСКАЕТСЯ ДО КАЖДОГО ТЕСТОВОГО МЕТОДА
# ЕСЛИ МЫ ХОТИМ ЗАФИКСИРОВАТЬ НАШЕ ПРИЛОЖЕНИЕ В КАКОМ-ТО СОСТОЯНИИ И НАЧАЛИ ТЕСТИРОВАТЬ ЕГО В ЭТОМ СОСТОЯНИИ
# ИСПОЛЬЗУЕМ ЭТОТ МЕТОД

# tearDown УНИЧТОЖИТЬ ЗАПУСКАЕТСЯ ПОСЛЕ КАЖДОГО ТЕСТОВОГО МЕТОДА
# ОНИ НУЖНЫ КОГДА МЫ ТЕСТИРУЕМ ПРИЛОЖЕНИЕ И ИСПОЛЬЗУЕМ ЛОЖНЫЕ ДАННЫЕ
# ЧТОБЫ УДАЛИТЬ ЛОЖНЫЕ ТЕСТОВЫЕ ДАННЫЕ ИСПОЛЬЗУЕМ ЭТОТ МЕТОД




class Shooter:
	def __init__(self, name, money = 1000, guns = []):
		self.name = name
		self.money = money
		self.guns = guns

	def get_cash(self, cash):
		self.money = self.money + cash
		if cash > 1000:
			return 'Let\'s go to the party!'
		else:
			return 'Let\'s go for more money!'

	def greet(self):
		if self.money > 100:
			return 'Hello! How are you?'
		else:
			return 'Hello! I need cash!'

	def buy_gun(self, new_gun, gun_cost):
		if self.money >= gun_cost:
			self.money -= gun_cost
			self.guns.append(new_gun)
			return 'Wow! Cool stuff!'
		else:
			return 'Sorry:( I have no money for this toy.'