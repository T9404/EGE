def F(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    else:
        return True


for i in range(100_000_000, 101_000_001):
    if i % 2 == 0:
        c = i//2
        
        if int(c**0.5)**2 == c and F(c**0.5) == True:
            c = int(c**0.5)
            print(i, c)
