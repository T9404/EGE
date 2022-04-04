f = open('27-70a.txt')
n = int(f.readline())


ost = [float('inf')]*5
s1, s2 = 0, 0


for _ in range(n):
    a, b = map(int, f.readline().split())
    s1 += min(a, b)
    s2 += max(a, b)
    ost[(max(a, b)-min(a, b)) % 5] = min(max(a, b) -
                                         min(a, b), ost[(max(a, b)-min(a, b)) % 5])


ma = 0

for x in ost:
    n = (s2-x)-(s1+x)
    if n % 5 == 0:
        ma = max(ma, n)

print(ma)
