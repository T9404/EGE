import math


f = open('C:\\Users\\XiaoMai\\Downloads\\27-36b.txt')
n = int(f.readline())


s = [0]

for _ in range(n):

    a = [int(x) for x in f.readline().split()]
    cmb = [math.gcd(a[0], a[1]), math.gcd(a[0], a[2]), math.gcd(a[2], a[1])]
    cmb2 = [a+b for a in s for b in cmb]
    s = {x % 10: x for x in sorted(cmb2)}.values()


m = max(x for x in s if (x % 10 == 0))

print(m)
