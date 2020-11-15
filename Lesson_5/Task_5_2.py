"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("Files/1_out.txt") as file:
    file_buf = file.readlines()
    lines = len(file_buf)
    words = 0
    for el in file_buf:
        words += len(el.split())
print(f"В файле {lines} строк, {words} слов.")
