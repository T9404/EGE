def f(x):
    x_2 = bin(x)[2:]
    x_2 = x_2[::-1]
    return int(x_2, 2)

for i in range(100, 1, -1):
    if f(i) == 13:
        print(i)
        break
