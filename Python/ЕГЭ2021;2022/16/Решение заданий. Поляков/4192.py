def f(n):
    if n == 0:
        return 1
    elif (n > 0 and n % 2 == 0):
        return f(n-1)+f(n-2)
    elif (n > 0 and n % 2 != 0):
        return 1.5*f(n-1)


print(len(str(int(f(15))))) 
