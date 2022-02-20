def f(n):
    if n <= 1:
        return 1
    elif (n > 1) and (n % 2 == 0):
        return 11 * n + f(n-1)
    else:
        return 11 * f(n - 2) + n


arr = [f(i) for i in range(35, 50+1) if f(i) % 2 == 0]

print(len(str(sum(arr))))
