from itertools import product
def f(x, y, a):
    return ( (3*y+2*x != 130) or (3*x > a) or (2 * y > a)  )

for a in range(1000, 0, -1):
    flag = 1
    for x, y in product(range(1, 1000), repeat=2):
        if not f(x, y, a):
            flag = 0
            break
    if flag:
        print(a)
        break
