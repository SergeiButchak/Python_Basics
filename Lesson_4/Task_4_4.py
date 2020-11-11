import random

arr = list([random.randint(0, 10) for el in range(30)])
new_arr = list([el for el in arr if arr.count(el) == 1])
print(f"Исходный массив: {arr}")
print(f"Новый массив: {new_arr}")

