f = open('C:\\Users\\XiaoMai\\Downloads\\27b.txt')
n = int(f.readline())


s = [0]

for _ in range(n):

    a = [int(x) for x in f.readline().split()]
    cmb = [x+b for x in s for b in a]
    s = {x % 256: x for x in sorted(cmb, reverse=True)}.values()


m = min(x for x in s if (x % 256 == 31))

print(m)
