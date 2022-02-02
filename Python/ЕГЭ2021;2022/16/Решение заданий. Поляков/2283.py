def F(n):
    if (n > 25):
        return n*n+4*n+3
    if (n <= 25) and (n % 3 == 0):
        return F(n+1)+2*F(n+4)
    if (n <= 25) and (n % 3 != 0):
        return F(n+2)+3*F(n+5)


count = 0

for a in range(1, 1001):
    k = F(a)
    sum = 0

    while k:
        sum += (k % 10)
        k = k//10
        
    if (sum == 24):
        count += 1

print(count)
