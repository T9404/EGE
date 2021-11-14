def f(a1, a2, x):
    return (not(a1 <= x <= a2)) <= (not (20 <= x <= 50) or (30 <= x <= 40))

m = float('inf')

for a1 in range(10, 70):
    for a2 in range(a1+1, 70+1):
        if all( f(a1, a2, x) == 1 for x in range(1, 100)):
            if m > a2 - a1:
                m = a2- a1
                start = a1
                end = a2

#print(start, end)
print(m)
