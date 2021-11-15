def f(n):
    if n < 5:
        return 1+2*n
    elif (n >= 5) and (n % 3 == 0):
        return 2*(n+1)*f(n-2)
    elif (n >= 5) and (n % 3 != 0):
        return 2*n+1+f(n-1)+2*f(n-2)

print(f(15))
