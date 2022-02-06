def F(n):
    a = set()

    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            a.add(i)
            a.add(n//i)

    if (len(a) != 0) and ((max(a)+min(a)) % 123 == 17):
        return max(a)+min(a)
    else:
        return 0


c = 0

for i in range(250201, 10000000000, 1):
    if (F(i) != 0):
        c += 1
        if (c <= 5):
            print(i, F(i))
        else:
            break
