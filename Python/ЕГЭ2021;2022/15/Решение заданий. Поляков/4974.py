def f(x, a1, a2):
    Q = 20 <= x <= 105
    P = 55 <= x <= 80
    A = a1 <= x <= a2
    return Q <= ( ( P == Q) or ( (not P) <= A) )

  
mik = float('inf')


for a1 in range(20, 106):
    for a2 in range(a1, 106):
        if all(f(x, a1, a2) == 1 for x in range(20, 106)):
            if mik > a2 - a1:
                mik = a2 - a1
                start = a1
                end = a2
            
            
print(start, end)
print('Answer: ', mik)
