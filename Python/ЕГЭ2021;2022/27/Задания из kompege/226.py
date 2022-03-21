f = open('C:\\Users\\XiaoMai\\Downloads\\27-B (7).txt')
n = int(f.readline())


chet = []
nechet = []
c = 0

for _ in range(n):
    x = int(f.readline())
    ost = x % 2

    if (ost == 0):
        for l in chet:
            if ((l+x) % 5 == 0):
                c += 1

        chet.append(x)

    if (ost == 1):
        for l in nechet:
            if ((l+x) % 5 == 0):
                c += 1

        nechet.append(x)

print(c)
