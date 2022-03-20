f = open('17.txt')


a = [int(x) for x in f.readlines()]
mak, k = 0, 0


for i in range(len(a)):
    if a[i] % 3 == 0 and a[i] % 7 != 0 and a[i] % 17 != 0 and a[i] % 19 != 0 and a[i] % 27 != 0:
        k += 1
        mak = max(a[i], mak)


print(k, mak)
