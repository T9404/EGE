def f(n):
    if n < 2:
        return 1
    elif n >= 2 and n % 3 == 0:
        return f(n/3)-1
    elif n >= 2 and n % 3 != 0:
        return f(n-1)+17


n = 1

while (not (f(n) == 110)):
    n += 1
    
print(n)
