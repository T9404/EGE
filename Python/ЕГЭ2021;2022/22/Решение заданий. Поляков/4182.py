for i in range(100000, 1, -1):
    x = i
    l, m = 0, 0

    while x > 12:
        l += 1
        x = x // 4
        m = x

    if l > m:
        l, m = m, l

    if l == 3 and m == 7:
        print(i)
        break
