"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str):
        buf = date_str.split('-')
        self.__day = int(buf[0])
        self.__month = int(buf[1])
        self.__year = int(buf[2])

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    @classmethod
    def date_split(cls, date_str):
        buf = date_str.split('-')
        day = int(buf[0])
        month = int(buf[1])
        year = int(buf[2])
        return day, month, year

    @classmethod
    def is_leap_year(cls, year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    @staticmethod
    def validate(date_str):
        days_in_mon = [31, 28, 31, 31, 31, 30, 31, 31, 30, 31, 30, 31]
        day_val = False
        mon_val = False
        day, month, year = Date.date_split(date_str)
        if 1 <= month <= 12:
            mon_val = True
        if mon_val:
            d = days_in_mon[month - 1]
            if month == 2 and Date.is_leap_year(year):
                d = d + 1
            if 1 <= day <= d:
                day_val = True
        else:
            if 1 <= day <= 31:
                day_val = True
        return day_val, mon_val


d = Date("21-12-2019")

print(d)
print(Date.date_split("21-12-2019"))
print(Date.is_leap_year(2020))
print(Date.validate("29-02-2020"))
print(Date.validate("29-02-2019"))
