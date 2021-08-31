def decto2(x):
    x2 = ''
    while x > 0:
        x2 += str(x % 2)
        x //= 2
    return x2[::-1]

def ok(n):
    return (n % 2 == 0) and\
         (decto2(n).count('1') == 3)\
         and ((n % 5 != 0) and (n % 8 == 0))

a = [n for n in range(64, 1024+1) if ok(n)]
print(len(a), max(a))
