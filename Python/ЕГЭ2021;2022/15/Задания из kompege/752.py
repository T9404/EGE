def f(x, a):
    return (   not ( not (x in a) and (x in (3, 6, 9, 12)) ) or ( x not in (1, 2, 3, 4, 5, 6))  )

a = set()

for x in range(1, 1000):
    if not f(x, a):
        a.add(x)
print(len(a))
