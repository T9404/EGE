P = {1, 2, 3, 4, 5, 6}
Q = {3, 5, 15}

A = set()

for x in range(100):
    f = (x in A) or ((x not in P) and (x in Q)) or (x not in Q)
    if f == 0:
        A.add(x)

print(len(A))
