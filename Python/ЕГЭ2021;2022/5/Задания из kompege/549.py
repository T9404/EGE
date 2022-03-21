def f(x):
    x_2 = bin(x)[2:]
    x_2 += x_2[-1]

    for _ in range(2):
        if x_2.count('1') % 2 == 0:
            x_2 += '0'
        else:
            x_2 += '1'

    return int(x_2, 2)


for i in range(1, 1000):
    if f(i) > 130:
        print(i)
        break
