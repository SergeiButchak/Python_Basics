"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

firm_dict = dict()
average_profit = 0
firm_cnt = 0
out_list = []
with open("Files/firms.txt", "r", encoding="utf-8") as file_in:
    while True:
        buf = file_in.readline().split()
        if not buf:
            break
        firm_dict[buf[0]] = buf[2]
        if int(buf[2]) - int(buf[3]) > 0:
            average_profit += int(buf[2])
            firm_cnt += 1
average_profit /= firm_cnt
out_list.append(firm_dict)
out_list.append({"average_profit": average_profit})
with open("Files/firms_out.txt", "w", encoding="utf-8") as file_out:
    json.dump(out_list, file_out)
