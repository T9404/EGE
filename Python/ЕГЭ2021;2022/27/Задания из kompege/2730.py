from itertools import combinations


f = open('27B.txt')
n = int(f.readline())


k_12, k_3, k_4, k_other = [], [], [], []


for _ in range(n):
    x = int(f.readline())

    if x % 12 == 0:
        k_12.append(x)

    elif x % 3 == 0:
        k_3.append(x)

    elif x % 4 == 0:
        k_3.append(x)

    else:
        k_other.append(x)


k_12.sort()
k_3.sort()
k_4.sort()
k_other.sort()


pick = k_12[-4:] + k_3[-4:] + k_4[-4:] + k_other[-4:]


mak = 0

for j in combinations(pick, 4):
    if (j[0]*j[1]*j[2]*j[3]) % 12 == 0:
        mak = max(sum(j), mak)

print(mak)
