def F(n):
    a = set()

    for i in range(1, int(n**0.5)+1):
        if (n % i == 0):
            a.add(i)
            a.add(n//i)

    return sum(a)


c, maxc = 0, 0

for i in range(2, 263000+1):
    if (F(F(i)) == i*2):
        c += 1
        maxc = max(maxc, i)

print(c, maxc)
