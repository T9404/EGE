# kompege 27 733 23.11.2020 ДЖОБС
f = open('C:\\Users\\XiaoMai\\Downloads\\27-A (1).txt')
n = int(f.readline())


sum, maxsr = 0, 0
a = [0]*10

for _ in range(n):
    x = int(f.readline())
    a[x] += 1


for k in range(0, 10):

    if (a[k] % 2 == 0):
        sum += a[k]*k
    else:
        sum += (a[k]-1)*k
        maxsr = max(maxsr, k)


if (a[5] > 1):
    print(sum+maxsr)
if (a[5] == 1):
    print(5)
