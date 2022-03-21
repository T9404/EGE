def f(x, s):
    m, x_s = 0, ''

    while x:
        x_s += str(x % s)
        x = x // s

    x_s = x_s[::-1]

    for i in x_s:
        if int(i) % 2 != 0:
            m += 1

    return m


d = [f(456, j) for j in range(2, 10+1)][::-1]
print(10 - d.index(max(d)))
