f = open('17.txt')
a = [int(x) for x in f.readlines()]


sr = sum(a) / len(a)
k, mak = 0, 0


for i in range(len(a)-1):
    summ = sum(map(int, str(a[i])+str(a[i+1])))

    if (summ**0.5) == int(summ**0.5) and (a[i]+a[i+1]) > sr:
        k += 1
        mak = max(mak, summ)


print(k, mak)
