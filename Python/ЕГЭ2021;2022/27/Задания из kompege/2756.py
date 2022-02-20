f = open('27B.txt')
n = int(f.readline())


os_12 = [0] * 100
ans = 0


for _ in range(n):
    x = int(f.readline())

    ost = (12 - (x % 100)) if (x % 100 <= 12) else (112 - (x % 100))

    if (os_12[ost] > x):
        ans = max(ans, os_12[ost]+x)


    os_12[x % 100] = max(x, os_12[x % 100])


print(ans)
