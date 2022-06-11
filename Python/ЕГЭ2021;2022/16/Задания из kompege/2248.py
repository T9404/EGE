'''
Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:

F(n) = n, при n ≤ 1,

F(n) = n + F(n / 3), когда n > 1 и делится на 3,

F(n) = n + F(n + 3) , когда n > 1 и не делится на 3.

Назовите минимальное значение n, для которого F(n) определено и больше 100.
'''
# https://prnt.sc/D0Gx9Fr0T2KG


from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 1:
        return n
    elif (n > 1) and (n % 3 == 0):
        return n + f(n // 3)
    elif (n > 1) and (n % 3 != 0):
        return n + f(n + 3)


for x in range(1, 1000):
    try:
        if f(x) > 100:
            print(x)
            break
    except:
        pass
