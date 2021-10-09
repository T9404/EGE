b = range(18, 52+1)
c = range(16, 41+1)

def f(x, a1, a2):
    return ( ( x in b) <= (a1 <= x <= a2) ) and ( (x not in c) or (a1 <= x <= a2))

m = float('inf')

for a1 in range(15, 53):
    for a2 in range(a1+1, 53):
        if all( f(x, a1, a2) == 1 for x in range(100, 6000)):
            if m > a2- a1:
                m = a2-a1
                start = a1
                end = a2

print(start, end)
print(m)


