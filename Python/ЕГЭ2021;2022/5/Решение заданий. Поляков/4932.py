def f(n):
    n_2 = bin(n)[2:]

    if n % 2 == 0:
        n_2 += bin(sum(map(int, n_2)))[2:]
    else:
        n_2 = '1' + n_2 + '00'

    return int(n_2, 2)


a = [i for i in range(1, 10000) if ( 500 <= f(i) <= 700)]
print(len(a))