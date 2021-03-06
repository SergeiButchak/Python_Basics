"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    __color = "Красный"

    def running(self, cycle):
        mode_time = {
            "Желтый": 2,
            "Зеленый": 4,
            "Красный": 7,
        }
        for i in range(cycle):
            print(self.__color)
            sleep(mode_time[self.__color])
            if self.__color == "Красный":
                self.__color = "Желтый"
            elif self.__color == "Желтый":
                self.__color = "Зеленый"
            else:
                self.__color = "Красный"


a = TrafficLight()
a.running(15)
