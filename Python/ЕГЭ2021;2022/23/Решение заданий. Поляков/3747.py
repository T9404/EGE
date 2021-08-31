from functools import lru_cache

@lru_cache
def f(start, x):
    if (x < start) or (x in [10, 15]):
        return 0
    if start == x:
        return 1
    k = f(start, x - 1) + f(start, x - 2)
    k += f(start, x - 3)
    return k

print('Ответ: ' + str(f(5, 11) * f(11, 18)))
