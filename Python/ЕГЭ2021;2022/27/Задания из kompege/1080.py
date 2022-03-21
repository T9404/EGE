from itertools import permutations


f = open('27-b.txt')
n = int(f.readline())


d = [[float('inf')]*4 for _ in range(9)]

for _ in range(n):
    x = int(f.readline())
    ost = x % 9

    d[ost].append(x)

    d[ost].sort(reverse=True)
    del(d[ost][0])


bigdata = []
for i in d:
    for z in i:

        if z != float('inf'):
            bigdata.append(z)


answer = min([(a+b+c+d)
             for a, b, c, d in permutations(bigdata, r=4) if (a+b+c+d) % 9 == 0])
             
print(answer)
