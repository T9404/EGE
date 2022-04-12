f = open('27B.txt')
n = int(f.readline())

s = {}
l = -1
for i in range(n):
    x = int(f.readline())
    c = [(sm + x, ln + 1, x, x - lst) for sm, ln, lst, r in s.values() if x - lst >= 1 and (x - lst == r or r == 0)] + [(x, 1, x, 0)]
    s = {x[0]%7: x for x in sorted(c, key = lambda x: x[1])}
    l = max(l, s.get(0, (0, 0))[1])

print(l)
