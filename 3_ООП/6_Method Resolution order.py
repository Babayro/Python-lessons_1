sfdgh = 'METHOD RESOLUTION ORDER РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ'
 # КАК НЕ ЗАПУТАТЬСЯ В УНАСЛЕДОВАНИИ КЛАССОВ
 #    A
 #   / \
 #  B   C
 #   \ /
 #    D

class A:
 # СТАТИЧНЫЕ МЕТОДЫ -ЭТО МЕТОДЫ В КОТОРЫХ НЕТ АТРИБУТОВ ДЛЯ ОБЪЕКТОВ КЛАССА И МЫ ИХ МОЖЕМ ОБЬЯВЛЯТЬ МЕТОДОМИ КЛАССАБ, НИЖЕ ПРИМЕР!!!
     @classmethod
     def some_method(cls):
         print('Method of class A')


class B(A):
    def some_method(self):
        print('Method of class B')


class C(A):
     def some_method(self):
         print('Method of class C')


class D(B,C):
# pass ПРОПУСК КОДА, Т.К МЫ ЗАКОМЕТИРОВАЛИ МЕТОД КЛАССА D, НАМ ВЫВОДИТСЯ СЛЕДУЩИЙ КЛАСС В ИИРАРХИИ В КОТОРОМ ЕСТЬ ДАННЫЙ МЕТОД, Т.E. КЛАСС "B"
     pass
     # def some_method(self):
     #     print('Method of class D')


some_objekt = D()
some_objekt.some_method()
print(D.mro())
print(D.__mro__)
help(D)