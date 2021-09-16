for i in range(81, 10**9):
    x = i
    s = 0
    while x > 0:
        s = s + x % 9
        x = x // 3
    if s==17:
        print(i)
        break