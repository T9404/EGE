def f(n):
    n_2 = bin(n)[2:]
    n_2 = n_2 + '10' if n % 2 == 0 else '1' + n_2 + '01'

    return int(n_2, 2)


for i in range(1, 10000):
    if f(i) >= 516:
        print(i)
        break
