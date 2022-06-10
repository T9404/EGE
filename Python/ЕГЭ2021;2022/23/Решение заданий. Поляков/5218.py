def f(s, e, k):
    if s > e or k > 3:
        return 0
    elif s == e:
        return 1
    else:
        return f(s + 2, e, k)+f(s * 3, e, k + 1)+f(s * 5, e, k + 1)


print(f(2, 200, 0))
