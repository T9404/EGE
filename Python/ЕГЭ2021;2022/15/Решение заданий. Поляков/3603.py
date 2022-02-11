from itertools import product


def f(x, y, a):
    return ((75 != 2 * x + 3 * y) or (a > 3 * x) or (a > 2 * y))


for a in range(0, 1000):
    flag = 1

    for x, y in product(range(0, 1000), repeat=2):
        if not f(x, y, a):
            flag = 0
            break
        
    if flag:
        print(a)
        break
