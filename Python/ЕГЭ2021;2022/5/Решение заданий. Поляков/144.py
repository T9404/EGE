minc = float('inf')


for k in range(10000, 100000):
    a = []
    t = k

    while t:
        a.append(t % 10)
        t = t//10
    a = a[::-1]

    s = ''
    s = str(min(a[0]+a[2]+a[4], a[1]+a[3]))+str(max(a[0]+a[2]+a[4], a[1]+a[3]))

    if (s == '621'):
        minc = min(minc, k)


print(minc)
