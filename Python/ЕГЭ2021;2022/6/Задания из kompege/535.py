for i in range(1, 10000):
    s = i
    n = 1

    while s < 94:
        s += 8
        n *= 2
        
    if n == 128:
        print(i)
        break
