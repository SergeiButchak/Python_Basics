def div(dividend, denominator):
    try:
        return dividend / denominator
    except ZeroDivisionError:
        return None


print(f"15/3 = {div(15, 3)}")
print(f"4523/34 = {div(4523, 34)}")
print(f"0/32 = {div(0, 32)}")
print(f"23/0 = {div(23, 0)}")
print(f"69/4 = {div(69, 4)}")
print(f"256/16 = {div(256, 16)}")
