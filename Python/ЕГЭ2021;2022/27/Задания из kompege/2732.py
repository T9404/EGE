f = open('27B.txt')
n = int(f.readline())


k_80 = [[] for _ in range(80)]


for _ in range(n):
    x = int(f.readline())

    k_80[x % 80].append(x)

    k_80[x % 80].sort()

    if len(k_80[x % 80]) == 3:
        del(k_80[x % 80][1])


mak = 0

for i in k_80:

    if len(i) == 2:
        mak = max(mak, i[1]-i[0])

print(mak)
