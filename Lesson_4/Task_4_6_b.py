from itertools import cycle

from sys import argv

if len(argv) == 3:
    try:
        a = argv[1]
        b = int(argv[2])
        for el in cycle(a):
            if b <= 0:
                break
            print(el)
            b -= 1

    except Exception as exc:
        print(exc)
else:
    print("Для запуска генератор требуется запустить скрипт с двумя аргументами <список> <количество "
          "повторений>")
