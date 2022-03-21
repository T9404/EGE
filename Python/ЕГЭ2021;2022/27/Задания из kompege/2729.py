from itertools import combinations


f = open('27B.txt')
n = int(f.readline())


numb = [[] for _ in range(11)]


for _ in range(n):
    x = int(f.readline())

    numb[x % 11].append(x)

    if len(numb[x % 11]) > 3:
        numb[x % 11].sort()
        del (numb[x % 11][-1])


pick = []

for i in numb:
    pick += i


mak = float('inf')

for i in combinations(pick, r=3):
    if sum(i) % 11 == 0:
        mak = min(mak, sum(i))

print(mak)
