def g(n):
    if n == 1:
        return 1
    elif ( n > 1):
        return f(n-1) + 2*g(n-1)

def f(n):
    if n == 1:
        return 1
    elif (n > 1):
        return f(n-1) - n * g(n-1)

print(g(18))
