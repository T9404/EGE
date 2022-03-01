from itertools import combinations


f = open('27-B.txt')
n = int(f.readline())


s = [0]


for _ in range(n):

    para = list(map(int, f.readline().split()))
    perm_para = [sum(i) for i in combinations(para, r=2)]

    cmb = [a + b for a in s for b in perm_para]
    s = {x % 4: x for x in sorted(cmb)}.values()


print(min(i for i in s if (i % 4 == 0)))
