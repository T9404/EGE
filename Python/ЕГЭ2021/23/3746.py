from functools import lru_cache

@lru_cache
def f(start, x):
    if (x < start) or (x == 12):
        return 0
    if start == x:
        return 1
    k = f(start, x - 1) + f(start, x - 3)
    if x % 2 == 0:
        k += f(start, x // 2)
    return k

print('Ответ: ' + str(f(3, 8) * f(8, 21)))
