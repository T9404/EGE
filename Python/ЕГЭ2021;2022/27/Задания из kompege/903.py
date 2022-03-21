f = open('27b.txt')
n = int(f.readline())


s = [0]

for _ in range(n):

    a = [int(x) for x in f.readline().split()]
    cmb = [x+b for x in s for b in a]
    s = {x % 3: x for x in sorted(cmb, reverse=True)}.values()


m = min(x for x in s if (x % 3 != 0))

print(m)
