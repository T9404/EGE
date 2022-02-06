# OMG ("_")
def f(n):  
    if n % 3 == 0:
        n //= 3
    else:
        n -= 1

    if n % 7 == 0:
        n //= 7
    else:
        n -= 1

    if n % 11 == 0:
        n //= 11
    else:
        n -= 1

    return n


a = set()

for i in range(2, 100000):
    if f(i) == 6:
        a.add(i)
        
print(len(a))
