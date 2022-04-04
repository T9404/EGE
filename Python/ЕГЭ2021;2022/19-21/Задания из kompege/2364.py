def f(a, c, m):
    if a > 20:
        return c % 2 == m % 2
    if c == m:
        return 0

    h = [f(a+1, c+1, m), f(a+2, c+1, m), f(a+3, c+1, m)]

    return any(h) if (c+1) % 2 == m % 2 else all(h)


t19, t20, t21 = [], [], set()

for a in range(1, 21):
    for m in range(1, 15):
        if f(a, 0, m) == 1:
            if m == 2:
                t19.append(a)
            if m == 5:
                t20.append(a)
            if m % 2 == 0:
                t21.add(a)


print(min(t19))
print(t20[0], t20[1], t20[2])
print(len(t21))
