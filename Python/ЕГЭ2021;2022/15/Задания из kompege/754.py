p = set(range(2, 21, 2))
q = set(range(5, 51, 5))


def f(x, a):
    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))


a = set(range(1, 1000))

for x in range(1, 1000):
    if not f(x, a):
        a.remove(x)

print(len(a))
