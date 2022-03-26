from itertools import product


d = ['']


for r in range(1, 3+1):
    d += [''.join(i) for i in product('0123456789', repeat=r)]


a = set()


for i in range(0, 9+1):
    for j in range(1, len(d)):

        x = int(format('123' + str(d[j]) + '567' + str(i)))

        if x % 169 == 0 and x <= 10**9:
            a.add((x, x // 169))


a = sorted(a, key=lambda x: x[0])

for i in a:
    print(*i)
