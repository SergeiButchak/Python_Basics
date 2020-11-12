from functools import reduce


def mul_el(prev_el, cur_el):
    return prev_el * cur_el


arr = list([el for el in range(100, 1001, 2)])
mul_arr = reduce(mul_el, arr)
print(f"Произведение элементов массива с четными числами от 100 до 100 \n {mul_arr}")
