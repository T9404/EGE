def f(s, e, k):
    if s > e:
        return 0

    elif s == e:
        return 1

    else:
        if k == 0:
            return f(s+1, e, 0)+f(s+2, e, 0)+f(s*2, e, k+1)

        elif k == 1:
            return f(s+1, e, 0)+f(s+2, e, 0)


print(f(1, 15, 0))
