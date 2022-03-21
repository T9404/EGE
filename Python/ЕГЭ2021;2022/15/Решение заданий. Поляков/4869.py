p = range(25, 37+1)
q = range(32, 47+1)


def f(x, a1, a2):
    return ((a1 <= x <= a2) and (x not in p)) <= ((x not in p) and (x in q))


mak = 0

for a1 in range(20, 50):
    for a2 in range(a1, 50):
        if all(f(x, a1, a2) == 1 for x in range(1, 100)):
            if mak < a2 - a1:
                mak = a2 - a1 
                start = a1
                end = a2 

print(start, end)
print(mak)