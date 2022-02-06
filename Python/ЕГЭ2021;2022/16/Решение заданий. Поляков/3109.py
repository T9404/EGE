def f(n):
    if n == 1:
        return 3
    elif n > 1:
        return 2 * f(n-1) - n + 1


print(f(21))
