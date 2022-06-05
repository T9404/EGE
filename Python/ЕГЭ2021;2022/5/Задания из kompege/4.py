def f(n):
    n_2 = bin(n)[2:]

    for i in range(2):
        n_2 += str(n_2.count('1') % 2)

    return int(n_2, 2)


for i in range(1000):
    if f(i) > 77:
        print(i)
        break