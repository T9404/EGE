def f(s, e):
    if s > e or s == 43:
        return 0
    elif s == e:
        return 1
    else:
        return f(s+2, e)+f(s+s-1, e)+f(s+s+1, e)

print(f(7, 63))
