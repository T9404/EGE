def func(n):
    if n <= 15:
        return n*n+11
    elif n > 15 and n % 2 == 0:
        return func(n//2) + n**3 - 5*n
    elif n > 15 and n % 2 != 0:
        return func(n-1) + 2 * n + 3


count = 0

for x in range(1, 1000+1):
    number = func(x)
    if str(number).count('6') >= 3:  
        count += 1

print(count)  
