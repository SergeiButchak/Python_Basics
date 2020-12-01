"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата.
"""


class Complex:
    def __init__(self, re=0, im=0):
        self.__re = re
        self.__im = im

    def __add__(self, other):
        re = self.__re + other.__re
        im = self.__im + other.__im
        return Complex(re, im)

    def __mul__(self, other):
        re = self.__re * other.__re - self.__im * other.__im
        im = self.__re * other.__im + self.__im * other.__re
        return Complex(re, im)

    def __str__(self):
        if self.__im < 0:
            return f"({self.__re} - {-1 * self.__im}i)"
        else:
            return f"({self.__re} + {self.__im}i)"


c_a = Complex(4, 3)
c_b = Complex(0, -1)
print(f"{c_a} + {c_b} = {c_a + c_b}")
print(f"{c_b} * {c_b} = {c_b * c_b}")
