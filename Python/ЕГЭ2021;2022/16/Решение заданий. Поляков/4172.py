from functools import lru_cache


@lru_cache(None)
def F(n):
    if n <= 3:
        return n+3
    if (n > 3) and (F(n-1) % 2 == 0):
        return F(n-2)+n
    if (n > 3) and (F(n-1) % 2 == 1):
        return F(n-2)+2*n


s = 0

for i in range(40, 51):
    s += F(i)

print(s)
