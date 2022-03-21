f = open('C:\\Users\\XiaoMai\\Downloads\\27-90b.txt')
zn = [int(x) for x in f.readline().split()]


def F(n):
    n = abs(n)
    s = 0

    while n > 0:
        s += (n % 3)
        n = n//3

    if s == 12:
        return 1
    else:
        return 0


n, k, d = zn[0], zn[1], zn[2]

len, c_os, sum, max_sum = 0, 0, 0, 0


s = [[float('inf')]*d for _ in range(k)]


for _ in range(n):
    x = int(f.readline())
    len += 1

    if (x < 0):
        c_os += F(x)

    sum += x

    if (len % d == 0) and (c_os % k == 0):
        max_sum = max(max_sum, sum)

    if (s[c_os % k][len % d] != float('inf')):
        max_sum = max(max_sum, sum-s[c_os % k][len % d])

    s[c_os % k][len % d] = min(s[c_os % k][len % d], sum)


print(max_sum)
