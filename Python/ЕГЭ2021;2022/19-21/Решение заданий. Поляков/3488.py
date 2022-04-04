# 1) Способ


from functools import lru_cache
from itertools import product


def move(h):
    a, b = h
    return (a+2, b), (a, b+2), (a*3, b), (a, b*3)


@lru_cache(None)
def f(h):
    new = lambda *values: (f(m) in values for m in move(h))
    if sum(h) >= 45:
        return 'win'
    if any(new('win')):
        return 'P1'
    if all(new('P1')):
        return 'V1'
    if any(new('V1')):
        return 'P2'
    if all(new('P1', 'P2')):
        return 'V2'


k19 = 0

for k, s in product(range(1, 43+1), repeat=2):
    if (k+s) <= 43 and (f((k, s)) == 'V1'):
        k19 += 1

print(k19)


# Вы дождались задачи, где не нужно в 19 писать any)
'''
Найдите количество решений, при котором Ваня выигрывает первым ходом при
любых П1. действиях. Т.Е. all(P1 move)
'''

print(min([i for i in range(1, 43+1) if f((4, i)) == 'P2']), end=' ')

print(max([i for i in range(1, 43+1) if f((4, i)) == 'P2' and (4 + i <= 43)]))

print(max(i for i in range(1, 43+1) if (f((13, i)) == 'V2' and (13+i <= 43))))




# 2) Способ


def f(a, b, c, m):
    if a+b >= 45:
        return c % 2 == m % 2
    if c == m:
        return 0

    h = [f(a+2, b, c+1, m), f(a, b+2, c+1, m),
         f(a*3, b, c+1, m), f(a, b*3, c+1, m)]

    return any(h) if (c+1) % 2 == m % 2 else all(h)


t19, t20, t21 = [], [], []
t1, t2 = [], []


for a in range(1, 44):
    for b in range(1, 44):
        for m in range(1, 6):
            if (a+b <= 43) and (f(a, b, 0, m) == 1):
                if m == 2:
                    t19.append(1)


for b in range(1, 44):
    for m in range(1, 6):
        if (4+b <= 43) and (f(4, b, 0, m) == 1):
            if m == 1:
                t1.append(b)
            if m == 3 and not b in t1:
                t20.append(b)


for b in range(1, 44):
    for m in range(1, 6):
        if (13+b <= 43) and (f(13, b, 0, m) == 1):
            if m == 2:
                t2.append(b)
            if m == 4 and not b in t2:
                t21.append(b)


print('----------------')
print(len(t19))
print(min(t20), max(t20))
print(t21[0])
