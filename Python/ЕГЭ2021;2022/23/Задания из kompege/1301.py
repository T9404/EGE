def f(s, e):
    if s < e:
        return 0
    elif s == e:
        return 1
    else:
        return f(s-2, e)+f(s-5, e)

print(f(23, 2))
