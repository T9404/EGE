from itertools import *


f = open('27-67b.txt')
n  = int(f.readline())


s = [0]

for _ in range(n):
    para = [int(x) for x in f.readline().split()]
    
    n_para = para[0]
    para = para[1:]
    para_i = []
    
    for i in range(1, n_para+1):
        d = list(combinations(para, r=i))

        for i in d:
            if sum(i) % 2 == 0 and sum(i) != 0:
                para_i.append(sum(i)) 


    cmb = [a + b for a in s for b in para_i]

    s = {x%5:x for x in sorted(cmb)}.values()

    
z = max(i for i in s if i % 5 != 0)

print(z)
