p = {1, 12}
q = {12, 13, 14, 15, 16}


def f(x, a):
    return (x not in a) <= ((x not in p) and (x not in q))


a = set()

for x in range(1, 1000):
    if not f(x, a):
        a.add(x)

print(len(a))
