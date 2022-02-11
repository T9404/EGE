for i in range(1, 10000):
    s = i
    n = 100
    while s - n >= 100:
        s += 20
        n += 40
    if s != i:
        print(i)
        break
