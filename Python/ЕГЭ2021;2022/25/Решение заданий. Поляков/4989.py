from itertools import product


d = ['']


for r in range(1, 2+1):
    d += [''.join(i) for i in product('0123456789', repeat=r)]


a = set()


for i, j in product(range(0, len(d)), repeat=2):
    
    x = int('12'+d[i]+'45'+d[j])

    if x <= 10**6 and x % 51 == 0:
        a.add((x, x//51))


a = sorted(a, key=lambda x: x[0])

for i in a:
    print(*i)
