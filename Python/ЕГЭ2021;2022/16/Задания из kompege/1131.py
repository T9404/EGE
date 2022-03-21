def f(n):
    if n == 1:
        return 1
    elif (n >= 2) and (n % 2 == 0):
        return f(n//2)+1
    elif (n >= 2) and (n % 2 != 0):
        return f(n-1) + n


d = [i for i in range(1, 1000) if f(i) == 19]
print(min(d))
