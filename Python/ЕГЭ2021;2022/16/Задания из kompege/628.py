def f(n):
    if n <= 18:
        return (n+3)
    elif (n % 3 == 0) and (n > 18):
        return (n//3)*f(n//3) + n - 12
    else:
        return f(n-1)+n*n+5


d = [i for i in range(1, 1000+1) if all(int(x) % 2 == 0 for x in str(f(i)))]
print(len(d))
