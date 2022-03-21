def f(n):
    n_2 = bin(n)[2:]
    condition_3 = bin(n)[2:]
    n_2 += n_2[-1]

    if condition_3.count('1') % 2 == 0:
        n_2 += '0'
    else:
        n_2 += '1'

    if n_2.count('1') % 2 == 0:
        n_2 += '0'
    else:
        n_2 += '1'

    return int(n_2, 2)


for i in range(1, 1000):
    if f(i) > 105:
        print(f(i))
        break
