def capital(s: str) -> str:
    buf = list(s)
    dif = ord('a') - ord('A')
    for ind in range(len(buf)):
        if ord(buf[ind]) >= ord('a') and ord(buf[ind]) <= ord('z'):
            buf[ind] = chr(ord(buf[ind]) - dif)
            break
    return "".join(buf)


string = input("Введите строку слов через пробел: ")
buf_str = string.split()
for i in range(len(buf_str)):
    buf_str[i] = capital(buf_str[i])
print(" ".join(buf_str))
