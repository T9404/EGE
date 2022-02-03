# 1 Решение

f = open('C:\\Users\\XiaoMai\\Downloads\\27-B.txt')
n = int(f.readline())


ost_c, ost_n = [0]*13, [0]*13
c = 0

for _ in range(n):
    x = int(f.readline())
    ost = x % 13

    if (x % 2 == 0):
        c += ost_c[ost]
        c += ost_n[ost]
    else:
        c += ost_c[ost]

    if (x % 2 == 0):
        ost_c[ost] += 1
    else:
        ost_n[ost] += 1


print(c)






# 2 Решение

f = open('27-B.txt')
n = int(f.readline())


a = []
c = 0

for _ in range(n):
    x = int(f.readline())

    for y in a:
        if abs(x-y) % 13 == 0 and (x*y) % 2 == 0:
            c += 1

    a.append(x)

print(c)
