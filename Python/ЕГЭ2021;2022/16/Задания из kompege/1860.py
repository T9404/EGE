def f(n):
    if n <= 1:
        return 0
    elif (n > 1) and (n % 2 != 0):
        return f(n-1)+3*n*n
    elif (n > 1) and (n % 2 == 0):
        return n/2 + f(n-1) + 2


print(int(f(49)))
