amount = 0
while True:
    string = input("Введите строку числе через пробел и/или 'q' для последующего завершения программы: ")
    list_str = string.split()
    buf_arr = []
    for el in list_str:
        try:
            buf_arr.append(int(el))
        except ValueError:
            continue
    amount += sum(buf_arr)
    print(f"Сумма чисел = {amount}")
    try:
        list_str.index("q")
        break
    except ValueError:
        continue
