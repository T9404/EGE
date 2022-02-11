from functools import lru_cache

@lru_cache
def f(start, x):
    if (x < start) or (x == 14):
        return 0
    if start == x:
        return 1
    k = f(start, x - 1) + f(start, x - 2)
    if x % 3 == 0:
        k += f(start, x // 3)
    return k

print('Ответ: ' + str(f(1, 10) * f(10, 15)))
