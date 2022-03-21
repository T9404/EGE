from itertools import product


def f3(x):
    x_3 = ''

    while x:
        x_3 += str(x % 3)
        x //= 3

    return int(x_3[::-1])


k, mak = 0, f3(100_000_000)  # по условию: на отрезке [1, 100 000 000]


for r in range(1, 18):
    for i in product('012', repeat=r):
        w = ''.join(i)

        if int(w) > mak:
            break

        if w[0] != '0' and (w.count('0') == 2):
            k += 1


print(k)


'''
Как догодаться до 3ой системы счисления и 2ух нулей?

1) В алгоритме присутствует целочисленное деление на 3
2) Выведите первые числа. Что у них общего в 3 с.с?
'''
