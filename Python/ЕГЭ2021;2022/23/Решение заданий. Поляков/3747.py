from functools import lru_cache

#1 Решение
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

#2 Решение
def f(s, e):
    if s == e:
        return 1
    elif (s  > e) or (s == 10) or (s == 15):
        return 0
    else:
        return f(s+1, e)+f(s+2, e)+f(s+3, e)
    
print('Answer: ', f(5, 11)*f(11, 18))
