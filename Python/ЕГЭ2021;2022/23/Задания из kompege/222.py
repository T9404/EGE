def f(s, e):
    if s > e or s == 6:
        return 0
    elif s == e:
        return 1
    else:
        return f(s+2, e)+f(s*3, e)

print(f(1, 25)*f(25, 63))
