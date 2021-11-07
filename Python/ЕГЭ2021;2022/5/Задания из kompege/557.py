def f(x):
    x_2 = bin(x)[2:]
    x_2 += x_2[-1]
    for i in range(2):
        x_2 += str(x_2.count('1') % 2)
    return int(x_2, 2)

for i in range(1, 10000):
    if f(i) > 144:
        print(f(i))
        break
