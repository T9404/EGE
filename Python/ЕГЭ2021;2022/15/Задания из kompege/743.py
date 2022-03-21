p = set(range(1, 12, 2))
q = set(range(3, 13, 3))


def f(x, a):
    return (x in p) <= (x not in q) or (x in a)


a = set()

for x in range(1, 1000):
    if not f(x, a):
        a.add(x)

print(sum(a))
