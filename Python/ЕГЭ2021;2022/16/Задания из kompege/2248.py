from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 1:
        return n
    elif (n > 1) and (n % 3 == 0):
        return n+f(n//3)
    elif (n > 1) and (n % 3 != 0):
        return n+f(n+3)


for x in range(1, 1000):
    try:
        if f(x) > 100:
            print(x)
            break
    except:
        pass
