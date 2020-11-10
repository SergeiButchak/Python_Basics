def my_func(arg_1, arg_2, arg_3):
    arr = [arg_1, arg_2, arg_3]
    arr.sort()
    return arr[1] + arr[2]


print(my_func(4, 7, 3))
print(my_func(67, 345, 7))
print(my_func(35, 5876, 9))
print(my_func(123, 523, 67))
print(my_func(34, 2, 56))
