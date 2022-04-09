from itertools import product


a = []


for i, j in product('0123456789ABCDEF', repeat=2):
    x = int('1' + i + 'DED' + j + 'CED', 16)
    m = int('79', 16)

    if x % m == 0:
        a += [[x, x // m]]


for i in sorted(a, reverse=True, key=lambda d: d[0]):
    print(*i)
