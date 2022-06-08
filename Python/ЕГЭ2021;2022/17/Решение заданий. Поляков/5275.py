f = open('17-1.txt')
a = [int(x) for x in f.readlines()]


min_15 = min(i for i in a if (i % 15 == 0) and (i > 0))
k, ans = 0, float('inf')


for i in range(len(a)-1):
    if (a[i] % 2 != 0) and (a[i+1] % 2 != 0):
        midd = (a[i] + a[i+1]) // 2  # оба числа нечётны
        if midd >= min_15:
            k += 1
            ans = min(ans, midd)


print(k, ans)
