def f(s, e, count):
    if count > 10:
        return 0

    elif (count == 10) and (s == e):
        return 1

    else:
        return f(s + 4, e, count + 1) + f(s + 7, e, count + 1) \
            + f(s // 2, e, count + 1)


print(f(1, 1, 0))
