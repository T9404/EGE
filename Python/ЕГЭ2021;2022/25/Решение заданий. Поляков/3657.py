def F(n):
    while n:
        c.append(n % 10)
        n = n//10


def G(n):
    w = set()
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            w.add(i)
            w.add(n//i)
    return len(w)


a = 0
c = []

for i in range(1000000, 1300000+1):
    F(i)

    if all(x < 3 for x in c) and (sum(c) % 10 == 0):
        a += 1

        if (a % 10 == 0):
            print(i, G(i))
            
    c = []
