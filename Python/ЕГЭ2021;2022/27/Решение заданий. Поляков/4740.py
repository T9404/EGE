f = open('27.txt')
N, K = map(int, f.readline().split())


def isPrime(x): 
    return all(x % j != 0 for j in range(2, int(x**0.5) + 1))


s = {0: (0, 0)}

m = 0


for _ in range(N):
    x = int(f.readline())

    rfux = (x < 0 and isPrime(-x))

    c = [(sm + x, cs + rfux) for sm, cs in s.values()] + [(x, rfux)]

    s = {x[1] % K: x for x in sorted(c)}

    m = max(m, s.get(0, (0, 0))[0])


print(m)
