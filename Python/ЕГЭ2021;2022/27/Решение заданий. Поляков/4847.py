# 1) Способ

f = open('C:\\Users\\XiaoMai\\Downloads\\27-92b.txt')
n = int(f.readline())


s = [float('inf')]*n

sum, count_os, max_sum = 0, 0, 0

for _ in range(n):
    x = int(f.readline())
    sum += x

    if (x > 0) and (x % 2 == 0):
        count_os += 1

    if count_os == 1:
        max_sum = max(max_sum, sum)

    if count_os > 1:
        max_sum = max(max_sum, sum-s[count_os-1])

    s[count_os] = min(s[count_os], sum)


print(max_sum)




# 2) Способ

f = open('27-92b.txt')
n = int(f.readline())


def func(x):
    if x > 0 and x % 2 == 0:
        return 1
    return 0


ans = float('-inf')
s = [[0, 0]]


for _ in range(n):
    x = int(f.readline())

    cmb = [[a + x, b + func(x)] for a, b in s] + [[x, func(x)]]
    s = {x[1] : x for x in sorted(cmb) if (x[1] <= 1)}

    if 1 in s:
        s1, k1 = s[1]
        ans = max(ans, s1)

    s = s.values()


print(ans)