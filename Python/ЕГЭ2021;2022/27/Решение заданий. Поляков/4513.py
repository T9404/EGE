f = open('27b.txt')
N = int(f.readline())


s = {0: (0, 0)}

m = 0


for _ in range(N):
    x = int(f.readline())

    c = [(sm + x, cs + (x % 5 == 0))
         for sm, cs in s.values()] + [(x, (x % 5 == 0))]

    s = {x[1] % 3: x for x in sorted(c)}

    m = max(m, s.get(0, (0, 0))[0])


print(m)
