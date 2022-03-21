def f(x, a, p, q):
    return (x not in a) <= ((x not in p) or (x not in q))


p = set(range(1, 4+1))
q = set(range(1, 6+1))


a = set()

for x in range(1, 10000):
    if not f(x, a, p, q):
        a.add(x)

print(len(a))
