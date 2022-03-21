# 1 Решение

f = open('27B.txt')
n = int(f.readline())


k_31 = []
k_other = []


for _ in range(n):
    x = int(f.readline())

    if x % 31 == 0:
        k_31.append(x)
    else:
        k_other.append(x)


print(min(k_31) * min(k_other))






# 2 Решение

f = open('27B.txt')
n = int(f.readline())


chet_31 = []
mina, answer = float('inf'), 0


for i in range(n):
    x = int(f.readline())

    if (x % 31 == 0):
        chet_31.append(x)
        chet_31.sort()
        chet_31 = chet_31[:2]
    mina = min(x, mina)


if len(chet_31) == 2:
    print(min(chet_31[0]*chet_31[1], mina*chet_31[0], mina*chet_31[1]))
else:
    print(mina*chet_31[0])
