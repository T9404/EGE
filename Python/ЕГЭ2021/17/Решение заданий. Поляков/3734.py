def decto2(x):
    x2 = ''
    while x > 0:
        x2 += str(x % 2)
        x //= 2
    return x2[::-1]

def ok(n):
    return (n % 2 == 1) and\
         (decto2(n).count('0') == 5)\
         and ((n % 3 == 0) and (n % 11 == 0))

a = [n for n in range(10, 9999+1) if ok(n)]
print(len(a), a[-1])
