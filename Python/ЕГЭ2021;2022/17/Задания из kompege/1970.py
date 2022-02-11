f = open('17 (1).txt')
a = [int(x) for x in f.readlines()]
k = 0
mak = float('-inf')
for i in range(len(a)-1):
    if abs(a[i]) % 3 == 0 or abs(a[i+1]) % 3 == 0:
        k += 1
        mak = max(a[i]+a[i+1], mak)
print(k, mak)
