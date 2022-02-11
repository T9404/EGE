def f(a, x):
    return ( x & 107 == 0) <= ( (x & 55 != 0) <= (x & a != 0))

for a in range(1, 1000):
    if all( f(a, x) == 1 for x in range(1, 1000)):
        print(a)
        break
