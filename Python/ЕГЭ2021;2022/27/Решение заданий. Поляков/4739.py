f = open('C:\\Users\\XiaoMai\\Downloads\\27-87b.txt')
a = [int(x) for x in f.readline().split()]


def F(n):
    c = 0
    n = abs(n)
    while n:
        if (n % 5 == 2):
            c += 1
        n = n//5
    return c


n, k = a[0], a[1]

s = [float('inf')]*k

m, sum, c = 0, 0, 0

for _ in range(n):
    x = int(f.readline())
    sum += x

    if (x < 0) and (F(x) == 0):
        c += 1

    if (c % k == 0):
        m = max(m, sum)

    m = max(m, sum-s[c % k])

    s[c % k] = min(s[c % k], sum)


print(m)
