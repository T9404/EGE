for i in reversed(range(10**6)):
    d = i
    n = 0
    s = 0
    while s <= 365:
        s = s + d
        n = n + 5
    if n==55:
        print(i)
        break