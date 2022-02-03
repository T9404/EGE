f = open('C:\\Users\\XiaoMai\\Downloads\\27-38b.txt')
n = int(f.readline())


a = [0]*10

for _ in range(n):
    a[int(f.readline())] += 1


sum, max_n = 0, 0

for i in range(0, 10):
    if (a[i] != 0):

        if (a[i] % 2 == 0):
            sum += a[i]*i
        else:
            sum += (a[i]-1)*i
            max_n = max(max_n, i)


sum += max_n
print(sum)
