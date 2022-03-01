f = open('27_B.txt')
n = int(f.readline())


s = [0]

for _ in range(n):
    x = int(f.readline())
    cmb = list(s) + [a + x for a in s] + [x]
    s = {x % 17: x for x in sorted(cmb)}.values()

print(max(i for i in s if (i % 17 == 0)))
