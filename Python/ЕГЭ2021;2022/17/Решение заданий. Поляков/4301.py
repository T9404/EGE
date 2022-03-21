f = open('17.txt')


d = [int(x) for x in f.readlines()]


k, mik = 0, float('inf')


for i in range(1, len(d)):

    a = int(d[i-1])
    b = int(d[i])

    if (a*b) > 0 and (abs(a+b) % 7 == 0):
        mik = min(a*b, mik)
        k += 1


print(k, mik)
