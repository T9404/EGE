f = open('27b.txt')
N, K = map(int, f.readline().split())


s = {0: (0, 0)}

m = 0


for _ in range(N):
    x = int(f.readline())

    rfux = (x > 0 and x % 2 == 0)

    c = [(sm + x, cs + rfux) for sm, cs in s.values()] + [(x, rfux)]

    s = {x[1] % K: x for x in sorted(c)}

    m = max(m, s.get(0, (0, 0))[0])


print(m)
