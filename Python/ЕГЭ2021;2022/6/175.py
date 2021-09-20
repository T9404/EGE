for i in reversed(range(10**6)):
    d = i
    n = 8
    s = 78
    while s <= 1200:
        s = s + d
        n = n + 2
    if n==46:
        print(i)
        break