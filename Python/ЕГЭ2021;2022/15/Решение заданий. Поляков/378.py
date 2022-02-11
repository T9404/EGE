def f(x, a):
    return (x & 29 != 0) <= (( x & 12 == 0) <= (x & a != 0))

for a in range(0, 1000):
    if all(f(x, a) == 1 for x in range(1, 1000)):
        print(a)
        break
