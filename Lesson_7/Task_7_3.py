"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
соответственно. В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Д
анный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:

    def __init__(self, c):
        self.__cells = c

    def __add__(self, other):
        return Cell(self.__cells + other.__cells)

    def __sub__(self, other):
        res = self.__cells - other.__cells
        if res > 0:
            return Cell(res)
        else:
            return None

    def __mul__(self, other):
        return Cell(self.__cells * other.__cells)

    def __truediv__(self, other):
        return Cell(int(self.__cells / other.__cells))

    def make_order(self, n):
        s = ""
        nl = '\n'
        cycl = int(self.__cells / n)
        mod = self.__cells % n
        s += f"{('*' * n + nl) * cycl}"
        s += f"{'*' * mod}"
        return s


order = 10
a = Cell(27)
b = Cell(10)
print(f"Клетка a\n{a.make_order(order)}")
print(f"Клетка b\n{b.make_order(order)}")
print(f"Клетка после сложенения\n{(a + b).make_order(order)}")
print(f"Клетка после вычитания\n{(a - b).make_order(order)}")
print(f"Клетка после умножения\n{(a * b).make_order(order)}")
print(f"Клетка после деления\n{(a / b).make_order(order)}")