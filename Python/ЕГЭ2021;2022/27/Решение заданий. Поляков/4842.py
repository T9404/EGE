f = open('27b.txt')
N, K, D = map(int, f.readline().split())


def k5(x):
    if x % 5 == 1:
        return 0

    if not(x):
        return 1

    return k5(x // 5)


s = {(0, 0): (0, 0)}

m = 0


for _ in range(N):
    x = int(f.readline())

    rfux = (x < 0 and k5(-x))

    c = [(sm + x, cs + rfux) for sm, cs in s.values()] + [(x, rfux)]

    s = {(x[0] % D, x[1] % K): x for x in sorted(c)}

    m = max(m, s.get((0, 0), (0, 0))[0])


print(m)
