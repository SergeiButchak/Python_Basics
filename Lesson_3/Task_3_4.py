def pow_v1(x, y):
    if y > 0:
        y *= -1
    return x**y


def pow_v2(x, y):
    y = abs(y)
    for i in range(y - 1):
        x *= x
    return 1/x


print(pow_v1(3, 2))
print(pow_v2(3, 2))

