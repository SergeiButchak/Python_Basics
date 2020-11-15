"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

employees = []
bad_employees = []
avg_salary = 0
with open("Files/emp.txt", "r") as file:
    while True:
        buf = file.readline().split()
        if not buf:
            break
        salary = int(buf[1])
        if salary < 20000:
            bad_employees.append(buf[0])
        avg_salary += salary
        employees.append(buf)
avg_salary /= len(employees)
print(f"Сотрудники имеющие оклад менее 20000: \n {bad_employees}")
print(f"Средний оклад сотрудников: \n {avg_salary}")
