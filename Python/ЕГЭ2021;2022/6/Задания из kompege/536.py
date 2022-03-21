for i in range(10000, 1, -1):
    s = i
    n = 1

    while s <= 45:
        s += 4
        n *= 2
        
    if n == 256:
        print(i)
        break
