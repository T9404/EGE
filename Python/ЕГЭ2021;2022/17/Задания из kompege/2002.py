f = open('17 (2).txt')


a = [int(x) for x in f.readlines()]
k, mak = 0, float('inf')


for i in range(len(a)-3):
    if a[i] > a[i+1] > a[i+2] > a[i+3]:
        if a[i] - a[i+3] > 1000:
            k += 1
            mak = min(a[i]+a[i+1]+a[i+2]+a[i+3], mak)


print(k, mak)
