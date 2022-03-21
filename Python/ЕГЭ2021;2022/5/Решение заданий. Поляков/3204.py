for n in range(2, 10000):
    a = bin(n)[2:]
    a += a[-2]
    a += a[1]
    r = int(a, 2)
    if r > 170:
        print(n)
        break
