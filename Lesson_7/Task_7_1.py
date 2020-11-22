"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    # __row_sz количество строк в матрице
    # __col_sz количество столбцов в матрице
    # __array список для хранения матрицы

    def __init__(self, arr: list):
        if type(arr) != list:
            raise TypeError
        self.__row_sz = len(arr)
        if type(arr[0]) != list:
            raise TypeError
        self.__col_sz = len(arr[0])
        for ind in range(1, len(arr)):
            if type(arr[ind]) != list:
                raise TypeError
            if self.__col_sz != len(arr[ind]):
                raise ValueError
        self.__array = list(arr)

    def __str__(self):
        s = ""
        for i in range(self.__row_sz):
            for j in range(self.__col_sz):
                s += f"{self.__array[i][j]:4} "
            s += "\n"
        return s

    def __getitem__(self, item):
        i, j = item
        return self.__array[i][j]

    def __add__(self, other):
        if self.__col_sz != other.__col_sz or self.__row_sz != other.__row_sz:
            raise ValueError
        result = list(self.__array)
        for i in range(self.__row_sz):
            for j in range(self.__col_sz):
                result[i][j] += other.__array[i][j]
        return Matrix(result)


a = Matrix([[4, 4, 5], [4, 5, 13], [1, 7, 5]])
b = Matrix([[1, 25, 7], [3, 96, 13], [13, 78, 6]])
print(f"Матрица а \n{a}")
print(f"Матрица b \n{b}")
print(f"Сумма матриц \n{a + b}")
