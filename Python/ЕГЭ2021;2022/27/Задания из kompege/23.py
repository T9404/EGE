f = open('27-B.txt')
n = int(f.readline())


s = [0]

for _ in range(n):
    para = list(map(int, f.readline().split()))
    cmb = [a + b for a in s for b in para]
    s = {x % 3: x for x in sorted(cmb)}.values()

print(max(i for i in s if (i % 3 != 0)))
