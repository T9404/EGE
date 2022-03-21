P = {2, 4, 6, 8, 10, 12}
Q = {4, 8, 12, 116}

A = set()

for x in range(100):
    f = (x in P) <= (((x in Q) and (x not in A)) <= (x not in P))
    if f == 0:
        A.add(x)

print(sum(A))
