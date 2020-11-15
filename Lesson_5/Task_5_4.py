"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

nums = {
    "Zero": "Ноль",
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять",
}
lines = []
with open("Files/num.txt") as file_in:
    while True:
        buf = file_in.readline().split()
        if not buf:
            break
        lines.append(buf)
with open("Files/num_out.txt", "w") as file_out:
    for el in lines:
        el[0] = nums[el[0]]
        file_out.write(" ".join(el) + "\n")
