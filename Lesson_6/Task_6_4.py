"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def __init__(self, color, name, speed):
        self.color = color
        self.name = name
        self.speed

    def go(self):
        print("Машина поехала")

    def stop(self):
        self.speed = 0
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Скорость превышена")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Скорость превышена")


class SportCar(Car):
    def show_speed(self):
        super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name, speed):
        super().__init__(color, name, speed)
        self.is_police = True


w = WorkCar("Зеленный", "ЗИЛ", 50)
w.go()
w.turn("право")
w.show_speed()
w.stop()
p = PoliceCar("Черный", "Hyundai", 60)
if p.is_police:
    print(f"Машина {p.name} полицейская")
print(f"Цвет машины {p.name} - {p.color}")
