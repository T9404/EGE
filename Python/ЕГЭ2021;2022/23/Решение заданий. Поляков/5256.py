def f(s, e, k):
    if s > e or k > 6:
        return 0
    elif s == e:
        return 1
    else:
        return f(s + 2, e, k + int((s + 2) % 2 == 1))+f(s * 2, e, k)+f(s * 3, e, k + int((s * 3) % 2 == 1))


print(f(1, 214, 0))
