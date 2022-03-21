def num_3(x):
    s = ''
    
    while x:
        s += str(x % 3)
        x //= 3

    return s[::-1]


def f(x):
    x_3 = num_3(x)
    x_3 += str(x % 3)

    return int(x_3, 3)


for i in range(1, 1000):
    if f(i) > 99:
        print(f(i))
        break
