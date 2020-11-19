"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income). Проверить работу примера на реальных
данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, positiion, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = positiion
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] * (1 + self._income["bonus"] / 100)


p = Position("Ivan", "Ivanov", "Manager", 10000, 15)
print(p.name)
print(p.surname)
print(p.position)
print(p.get_full_name())
print(p.get_total_income())
