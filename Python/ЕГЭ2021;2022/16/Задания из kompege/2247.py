def f(n):
    if n < 3:
        return n+1
    elif (n % 2 == 0):
        return f(n-2)+n-2
    elif (n % 2 != 0):
        return f(n+2)+n+2

k = 0
for z in range(1, 10000):
    try:
        if len(str(f(z))) == 5:
            k+=1
    except:
        pass

print(k)
