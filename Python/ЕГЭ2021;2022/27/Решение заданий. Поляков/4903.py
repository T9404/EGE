f = open('27-95b.txt')
n = int(f.readline())


count = [0]*n
ans, k5, k7 = 0, 0


for _ in range(n):
    x = int(f.readline())

    if x % 5 == 0:
        k5 += 1
    if x % 7 == 0:
        k7 += 1

    if k5 == k7:
        ans += 1

    ans += count[k5-k7]

    count[k5-k7] += 1


print(ans)
