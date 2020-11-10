# 1
print("Задание N1")
p = [2, 34.56, "text", [2, 3]]
print(f"Имеется список {p}")
for el in p:
    print(f"Элемент {el} имеет тип {type(el)}")

# 2
print("Задание N2")
lst = []
list_size = int(input("Введите количество элементов в списке: "))
for i in range(list_size):
    lst.append(input(f"Введите значение элемента {i}: "))
print(f"Введенный список: {lst}")
for i in range(0, len(lst), 2):
    if i < len(lst) - 1:
        buf = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = buf
print(f"Измененный список: {lst}")

# 3
print("Задание N3 списки")
season_by_month = ("зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима")
while True:
    num = int(input("Введите номер месяца от 1 до 12: "))
    if (num > 0) and (num < 13):
        break
    else:
        print("Введенное значение должно быть в диапазоне от 1 до 12")
print(f"Введенный месяц соответствует времени года '{season_by_month[num]}'")

print("Задание N3 словарь")
season_by_month = {
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень",
    12: "зима"
}
while True:
    num = int(input("Введите номер месяца от 1 до 12: "))
    if (num > 0) and (num < 13):
        break
    else:
        print("Введенное значение должно быть в диапазоне от 1 до 12")
print(f"Введенный месяц соответствует времени года '{season_by_month.get(num)}'")

# 4
print("Задание N4")
string = input("Введите строку: ")
string = string.split(" ")
for ind, el in enumerate(string):
    print(f"{ind} {el:>10.10}")

# 5
print("Задание N5")
my_list = [7, 5, 3, 3, 2]
print(f"Исходный массив {my_list}")
num = int(input("Введите число: "))
for ind in range(len(my_list)):
    if num > my_list[ind]:
        my_list.insert(ind, num)
        break
else:
    my_list.append(num)
print(f"Массив после вставки {my_list}")

# 6
print("Задание N6")
count_item = 0
items = list()
count = int(input("Введите количество товаров: "))
for i in range(count):
    count_item += 1
    print(f"Введите характеристики для товара {count_item}")
    name = input("Введите наименование товара: ")
    price = int(input("Введите цену: "))
    amount = int(input("Введите количество: "))
    unit = input("Введите единицу измерения: ")
    items.append((count_item, {"название": name, "цена": price, "количество": amount, "eд": unit}))
print(items)
if count_item > 0:
    item_prop = list(items[0][1].keys())
    analitic = dict()

    for ind in item_prop:
        analitic.update({ind: set()})
    for g in items:
        for p in item_prop:
            analitic.get(p).add(g[1].get(p))
    print(analitic)
