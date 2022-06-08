f = open('17-205.txt')
a = [int(x) for x in f.readlines()]


k, mak = 0, float('-inf')


for i in range(len(a)-1):
    if a[i] % 7 == 0 or a[i+1] % 7 == 0:
        # могут быть отрицательные суммы
        if abs(a[i]+a[i+1]) % 100 == 19:
            k += 1
            mak = max(mak, a[i]+a[i+1])


print(k, mak)
