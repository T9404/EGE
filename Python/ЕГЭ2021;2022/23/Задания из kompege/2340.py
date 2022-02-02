def f(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        return f(s+2, e)+f(s+4, e)+f(s+5, e)


m = [i for i in range(32, 60) if (f(31, i) == 1001)]
print(*m)
