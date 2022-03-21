f = open('17.txt')


d = [int(x) for x in f.readlines()]


k, mik = 0, float('inf')


for i in range(1, len(d)-1):

    a = int(d[i-1])
    b = int(d[i])
    c = int(d[i+1])

    if (a < b < c):
        mik = min(c-a, mik)
        k += 1


print(k, mik)
