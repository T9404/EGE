from itertools import product

def f(a, x, y):
    return (x > 39) or (y > 26) or (2*x+4*y < a)

for a in range(1, 1000):
    ok = 1
    for x,y in product(range(1, 100), repeat=2):
        if not f(a, x, y):
            ok = 0
            break
    if ok == 1:
        print(a)
        break
