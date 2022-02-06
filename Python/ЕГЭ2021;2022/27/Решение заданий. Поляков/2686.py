f = open('27-26a.txt')
n = int(f.readline())


s = [0]

for _ in range(n):

    para = [int(x) for x in f.readline().split()]
    cmb = [a + b for a in s for b in para]
    s = {x % 16: x for x in sorted(cmb, reverse=True)}.values()


m = min(x for x in s if x % 16 == 15)

print(m)
