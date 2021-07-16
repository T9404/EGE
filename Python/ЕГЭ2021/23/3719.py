from functools import lru_cache

@lru_cache(None)
def f(start, x):
    if (x < start):
        return 0
    if start == x:
        return 1
    k = f(start +2, x) + f(start +3, x )
    k += f(start * 4, x)
    return k

print('Ответ: ' + str(f(1, 16)))
