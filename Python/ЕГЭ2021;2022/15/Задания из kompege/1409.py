p = set(range(2, 21, 2))
q = set(range(3, 31, 3))
r = set(range(12, 61, 12))

def f(x, a):
    return (x not in a) <= ( ( ( x in p) and (x in q) ) <= (x in r) )

a = []
for x in range(1, 1000):
    if not f(x, a):
        a.append(x)
z = 1
for i in range(len(a)):
    z *= a[i]
print(z)
