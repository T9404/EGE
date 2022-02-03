f = open('C:\\Users\\XiaoMai\\Downloads\\27_B (4).txt')
n = int(f.readline())


a = [int(f.readline()) for _ in range(4)]
p = [0]*117


sum_all = sum(a)
sum_q, count = 0, 0

for _ in range(n-4):
    x = int(f.readline())
    sum_all += x

    if sum_all % 117 == 0:
        count += 1

    count += p[(sum_all) % 117]

    sum_q += a[0]
    p[sum_q % 117] += 1

    a.pop(0)
    a.append(x)


print(count)
