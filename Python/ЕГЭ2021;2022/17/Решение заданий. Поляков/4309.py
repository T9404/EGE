f = open('17.txt')


d = [int(x) for x in f.readlines()]


k, mik = 0, float('inf')


for i in range(1, len(d)-2):  
    a, b, c, e = int(d[i-1]), int(d[i]), int(d[i+1]), int(d[i+2])  

    if (a > b > c > e):
        if (abs(a-e) > 1000):
            mik = min(a+b+c+e, mik)
            k += 1


print(k, mik)
