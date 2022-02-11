P = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

A = set()

for x in range(100):
    f = ((x in P) <= (x in A)) or ((x not in A) <= (x not in Q))
    if f == 0:
        A.add(x)

print(len(A))
