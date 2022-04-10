from itertools import product


def f_9(x):
    x_9 = []

    while x:
        x_9.append(x % 9)
        x //= 9

    return ''.join(map(str, x_9[::-1]))


def sys_numb(x):
    x_9 = f_9(x)

    for i in range(len(x_9)-1):
        if x_9[i] < x_9[i+1]:
            return False

    return x, sum(map(int, x_9))


a = set()


for i, j, m, n in product('0123456789 ', repeat=4):
    x = int(('3' + i + '458' + j + m + n + '3').replace(' ', ''))

    if x <= 10**9 and sys_numb(x):
        a.add(sys_numb(x))


for i in sorted(a, key=lambda d: d[0]):
    print(*i)
