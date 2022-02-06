def F(n):
    a = set()

    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            a.add(i)
            a.add(n//i)

    s = sum(list(a))

    if (s != 0) and (str(s) == str(s)[::-1]):
        return max(list(a))
    else:
        return 0


c = 0

for i in range(520001, 10000000):
    if F(i) != 0:
        c += 1
        
        if (c <= 5):
            print(i, F(i))
        else:
            break
