a = set()

def f(n):
    if n == 0:
        return 0
    elif (n > 0) and (n % 2 ==0):
        return f(n//2) - 1
    elif (n > 0) and (n % 2 != 0):
        return 3 + f(n-1)

for n in range(1, 1000):
    a.add(f(n))

print(len(a))
