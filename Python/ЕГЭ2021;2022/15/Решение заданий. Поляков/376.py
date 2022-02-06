def f(x, a1, a2):
    return ((4 <= x <= 15) and (12 <= x <= 20)) <= (a1 <= x <= a2)


mik = float('inf')

for a1 in range(1, 100-1):
    for a2 in range(a1+1, 100):
        if all(f(x, a1, a2) for x in range(1, 100)):
            if a2-a1 < mik:
                mik = a2-a1
                start = a1
                end = a2
                
print(start, end)
print(mik)
