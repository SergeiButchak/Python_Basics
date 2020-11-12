def fact(num):
    mul = 1
    for el in range(1, num + 1):
        mul *= el
        yield mul


for n in fact(4):
    print(f"{n}")
