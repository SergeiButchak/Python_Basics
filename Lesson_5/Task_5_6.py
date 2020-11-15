"""
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""

import re

lectures = dict()
with open("Files/lectures.txt", "r", encoding="utf-8") as file:
    while True:
        buf = file.readline().split()
        if not buf:
            break
        lecture = buf[0][:-1]
        hours = 0
        for ind in range(1, len(buf)):
            num = re.search(r"\d*", buf[ind]).group(0)
            if num != "":
                hours += int(num)
        lectures[lecture] = hours
print(lectures)
