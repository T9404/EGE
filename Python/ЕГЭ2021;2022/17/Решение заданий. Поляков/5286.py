f = open('17-336.txt')
a = [int(x) for x in f.readlines()]


M = max(i for i in a if i % 37 == 0)
k, mik = 0, float('inf')


for i in range(len(a)-1):
    if a[i] % M == 0 or a[i+1] % M == 0:
        if (a[i]+a[i+1]) % M > 30:
            k += 1
            mik = min(mik, a[i]+a[i+1])


print(k, mik)
