def f(x, a):
    return ((x % 175 == 0) <= (x % 25 != 0)) or (2*x+a >= 1780)


for a in range(1, 10000):
    if all(f(x, a) == 1 for x in range(1, 10000)):
        print(a)
        break
