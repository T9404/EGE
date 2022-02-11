def f(x):
    s = x
    n = 1
    while s <= 80:
        s += 7
        n *= 3
    if n == 81:
        return 1
    else:
        return 0

for i in range(10000, 1, -1):
    if f(i):
        print(i)
        break
