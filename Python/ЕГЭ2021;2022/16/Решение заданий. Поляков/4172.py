'''
Алгоритм вычисления значения функции F(n), где n – целое число, 
задан следующими соотношениями:
F(n) = n + 3, при n ≤ 3
F(n) = F(n – 2) + n, при n > 3 и четном значении F(n-1),
F(n) = F(n – 2) + 2•n, при n > 3 и нечетном значении F(n-1).
Определите сумму значений, являющихся результатом вызова функции для 
значений n в диапазоне [40; 50].
'''
# https://prnt.sc/dLAjngtFYCIn


from functools import lru_cache


@lru_cache(None)
def F(n):
    if n <= 3:
        return n + 3
    if (n > 3) and (F(n - 1) % 2 == 0):
        return F(n - 2) + n
    if (n > 3) and (F(n - 1) % 2 == 1):
        return F(n - 2) + 2 * n


arr = [F(i) for i in range(40, 50+1)]
print(sum(arr))
