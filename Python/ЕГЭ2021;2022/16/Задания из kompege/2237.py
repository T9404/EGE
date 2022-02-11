def f(n):
    if n == 0:
        return 0
    elif (n > 0) and (n % 2 == 0):
        return f(n//2)
    elif (n % 2 != 0):
        return 1 + f(n-1)


d = [n for n in range(1, 500+1) if f(n) == 8]
print(len(d))
