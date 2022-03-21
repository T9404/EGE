for i in range(10000, 1, -1):
    s = i
    n = 3
    
    while s < 220:
        s += 6
        n += 3

    if n > 40:
        print(i)
        break
