# 1) Решение

f = open('C:\\Users\\XiaoMai\\Downloads\\27_B (1).txt')
n = int(f.readline())


max_sum = 0
s = [[0, 0]]*3

for _ in range(n):
    x = int(f.readline())

    ost_5 = int(x % 5 == 0)

    comb = [[x+a, b+ost_5] for a, b in s]+[[x, ost_5]]
    s = {x[1] % 3: x for x in sorted(comb)}.values()

    for a, b in s:
        if (b % 3 == 0) and (a > max_sum):
            max_sum = a


print(max_sum)






# 2) Решение

f = open('27_B.txt')
n = int(f.readline())


sums = [float('inf')] * 3
s, k_5, answer = 0, 0, 0


for _ in range(n):
    x = int(f.readline())
    s += x

    if x % 5 == 0:
        k_5 += 1
    if k_5 % 3 == 0:
        answer = max(s, answer)

    answer = max(answer, s - sums[k_5 % 3])

    sums[k_5 % 3] = min(sums[k_5 % 3], s)


print(answer)
