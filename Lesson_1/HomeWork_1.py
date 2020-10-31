# 1
print("Задание N1")
cur_year = 2020
birth = int(input("Введите свой год рождения: "))
name = input("Введите ваше имя: ")
print(f"Здравствуйте {name}, ваш возраст {cur_year - birth}")

# 2
print("Задание N2")
seconds = int(input("Введите количество секунд: "))
minutes = seconds // 60
hour = minutes // 60
print(f"Время {hour % 24:02}:{minutes % 60:02}:{seconds % 60:02}")

# 3
print("Задание N3")
num = input("Введите число n: ")
summary = int(num) + int(num + num) + int(num + num + num)
print(f"Сумма n + nn + nnn = {summary}")

# 4
print("Задание N4")
num = int(input("Введите число n: "))
digit = num % 10
max_digit = digit
while num > 0:
    if max_digit < digit:
        max_digit = digit
    num //= 10
    digit = num % 10
print(f"Максимальная цифра в числе {max_digit}")

# 5
print("Задание N5")
debit = int(input("Введите доход компании: "))
credit = int(input("Введите расход компании: "))
if credit > debit:
    print("Компания работает в убыток")
elif credit == debit:
    print("Компания работает на себя")
else:
    print("Компания работает с прибылью")
    print(f"Рентабельность компании: {(debit - credit) / debit * 100:.2f}%")
    employees = int(input("Введите количество сторудников: "))
    print(f"Прибыль фирмы в расчете на сотрудника {(debit - credit) / employees:.2f}")

# 6
print("Задание N6")
a = int(input("Введите пройденное расстояние за 1-й день: "))
b = int(input("Введите требуемое расстояние: "))
day = 1
while a < b:
    a *= 1.1
    day += 1
print(f"На {day}-й день спортсмен достигнет результата — не менее {b} км")
