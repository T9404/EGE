p = range(17, 54+1)
q = range(37, 83+1)


def f(x, a1, a2):
    return (x in p) <= (((x in q) and not(a1 <= x <= a2)) <= (x not in p))


m = float('inf')

for a1 in range(10, 90):
    for a2 in range(a1+1, 90):
        if all(f(x, a1, a2) == 1 for x in range(10, 6000)):
            if m > a2-a1:
                z = a2
                c = a1
                m = a2-a1

print(c, z)
print(m)
