import random

arr = list([random.randint(0, 100) for el in range(30)])
new_arr = list([arr[ind] for ind in range(1, len(arr)) if arr[ind] > arr[ind - 1]])
print(f"Исходный массив: {arr}")
print(f"Новый массив: {new_arr}")
