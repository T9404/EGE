def decto2(x):
    x2 = ''
    while x > 0:
        x2 += str(x % 2)
        x //= 2
    return x2[::-1]

def ok(n):
    s = 0
    x = int(decto2(n))
    while x > 0:
        s += x % 10
        x //= 10
    
    return (n % 2 == 0) and (s == 5) and (n % 10 != 0)

a = [n for n in range(31, 2047+1) if ok(n)]
print(len(a), max(a))
