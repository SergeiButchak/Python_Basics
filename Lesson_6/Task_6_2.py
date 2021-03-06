"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_mass(self, thick, mass_square):
        return self.__width * self.__length * thick * mass_square


r = Road(5000, 20)
print(f"Масса асфальта для дороги: {r.calc_mass(5, 25) / 1000} т")
