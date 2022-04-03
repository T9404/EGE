def f(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        s_num = sum(map(int, str(s)))
        return f(s+2, e)+f(s+s_num, e)

print(f(3, 29)*f(29, 68))