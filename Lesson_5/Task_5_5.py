"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint
numbers = list([randint(0, 100) for i in range(50)])
sum_arr = sum(numbers)
with open("Files/num_out.txt", "w") as file:
    for el in numbers:
        file.write(str(el) + " ")
print(f"Сумма записанных в файл чисел: {sum_arr}")
