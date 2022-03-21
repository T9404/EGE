def f(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        return f(s+1, e)+f(s*2, e)+f(s**2, e)


print(f(5, 154))
