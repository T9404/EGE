def f(s, e, add_1):
    if s > e:
        return 0

    elif s == e:
        return 1

    else:

        if add_1 == 1:
            return f(s+3, e, 0)+f(s*2, e, 0)

        elif add_1 < 1:
            return f(s+1, e, 1)+f(s+3, e, 0)+f(s*2, e, 0)


print(f(3, 30, 0))
