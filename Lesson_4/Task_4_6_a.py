from itertools import count
from sys import argv

if len(argv) == 3:
    try:
        a = int(argv[1])
        b = int(argv[2])
        for el in count(a):
            if el > b:
                break
            print(el)

    except Exception as exc:
        print(exc)
else:
    print("Для запуска генератор требуется запустить скрипт с двумя аргументами <начальное значение> <максимальное "
          "значение>")
