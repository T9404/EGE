def F(n):
    if n == 0:
        return 0
    if (n % 2 == 0) and (n > 0):
        return F(n//2)-1
    if (n % 2 == 1) and (n > 0):
        return 2+F(n-1)


c = 0

for i in range(0, 1000):
    if (F(i) == 3):
        c += 1

print(c)
