def F(n):
    if all(n % d != 0 for d in range(2, int(n**0.5)+1)):
        return True


c = 0


for i in range(450001, 490000):
    a = set()
    m = 0

    for k in range(2, int(i**0.5)+1):
        if (i % k == 0):
            if (F(k) == True):
                a.add(k)
            if (F(i//k) == True):
                a.add(i//k)

    if len(a) != 0:
        m = max(a)-min(a)

    if (m != 0) and (m % 29 == 11):
        c += 1
        
        if (c < 5):
            print(i, m)
