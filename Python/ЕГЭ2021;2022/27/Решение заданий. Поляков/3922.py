f = open('файлик')
n = int(f.readline())


a = sorted([int(f.readline()) for _ in range(n)])

maxl = 0

for e in range(len(a)):
    c = a[e]
    len = 1
    k = 1

    while (k <= 100):
        c += k

        if (c in a):
            len += 1
            maxl = max(maxl, len)
        else:
            len = 1
            c = a[e]
            k += 1


print(maxl)
