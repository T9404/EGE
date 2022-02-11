def f(x):
    if x <= 3:
        return 3
    elif (x > 3) and (x % 2 == 0):
        return f(x//2)+5
    else:
        return f(x-1)-f(x-2)

print(f(20))
