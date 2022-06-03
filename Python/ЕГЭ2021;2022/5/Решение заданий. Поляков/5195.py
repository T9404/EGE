def f(n):
    n_2 = bin(n)[2:]
    n_2 = '1' + n_2 + '00' if n_2.count('1') % 2 == 0 else '11' + n_2

    return int(n_2, 2)


for i in range(1, 10000):
    if f(i) >= 412:
        print(i)
        break
