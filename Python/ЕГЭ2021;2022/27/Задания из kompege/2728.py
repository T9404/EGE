from itertools import combinations


f = open('27B.txt')
n = int(f.readline())


k_23 = [[], []]
k_other = [[], []]


for _ in range(n):
    x = int(f.readline())

    if x % 23 == 0:
        k_23[x % 2].append(x)
    else:
        k_other[x % 2].append(x)


pick = []

for i in range(2):
    try:
        pick += [max(k_other[i])]
        pick += [max(k_23[i])]

    except:
        pass


mak = 0

for i in combinations(pick, r=2):
    if ((i[0] % 23 == 0) + (i[1] % 23 == 0)) >= 1:
        if sum(i) % 2 == 0:
            mak = max(sum(i), mak)

print(mak)
