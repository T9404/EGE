# 1) Способ

f = open('C:\\Users\\XiaoMai\\Downloads\\27-53b.txt')
n = int(f.readline())


d1 = [float('inf')]*3
d2 = [float('inf')]*3

min_sum = float('inf')

for _ in range(n):
    x = int(f.readline())

    for i in range(3):
        if ((d2[i]+x) % 3 == 0):
            min_sum = min(min_sum, d2[i]+x)

    for i in range(3):
        d2[(i+x) % 3] = min(d2[(i+x) % 3], d1[i]+x)

    d1[x % 3] = min(d1[x % 3], x)


print(min_sum)






# 2) Способ (опасный!)

from itertools import combinations


f = open('27-53b.txt')
n = int(f.readline())


numbers = []

for _ in range(n):
    x = int(f.readline())

    numbers.append(x)
    numbers.sort()

    if len(numbers) > 100: # danger
        numbers = numbers[:-1]


ans = float('inf')

for a, b, c in combinations(numbers, r=3):
    if (a+b+c) % 3 == 0:
        ans = min(a+b+c, ans)

print(ans)






# 3) Способ Лёни https://vk.com/leonid_shastin

from itertools import combinations


d = [[],[],[]]

for x in sorted([int(x) for x in open('27-53b.txt')][1:]):
    if len(d[x % 3]) < 3:
        d[x%3] += [x]

print(min(sum(x) for x in combinations(d[0][:3]+d[1][:3]+d[2][:3], 3) if sum(x)%3 == 0))
