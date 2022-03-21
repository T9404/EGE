def f(x):
    a = set()

    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            a |= {i, x//i}

    b = sorted([i for i in a if (i % 2 == 0)])
    
    if len(b) == 4:
        return b[-1], b[-2]
    else:
        return False


for i in range(190201, 190260+1):
    if f(i):
        print(*f(i))
