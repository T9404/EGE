f = open('27-B.txt')
n = int(f.readline())


s = [0]

for _ in range(n):
    para = list(map(int, f.readline().split()))
    cmb = [a + b for a in s for b in para]
    s = {x % 5: x for x in sorted(cmb, reverse=True)}.values()

print(min(i for i in s if (i % 5 != 0)))
