from itertools import product


def f(x, n):
    x_n = ''
    while x:
        x_n += str(x % n)
        x //= n
    d = [(str(i)+str(i)) for i in range(n)]
    for i in d:
        if i in x_n:
            return False
    return True


k = 0
for i in range(2, 10+1):
    if f(1988, i):
        k += i
print(k)
