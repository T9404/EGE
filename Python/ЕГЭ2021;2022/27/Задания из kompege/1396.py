f = open('27-B.txt')
n = int(f.readline())

s = [0]

for _ in range(n):
    para = [ int(x) for x in f.readline().split() ]
    cmb = [a + b for a in s for b in para]
    s = {x%246:x for x in sorted(cmb, reverse=True) }.values()
z = min(i for i in s if (i % 123 != 0 and i % 2 == 0) )
print(z)
