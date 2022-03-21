def f(x):
    d = []
    
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.append(i)
            d.append(x//i)

    return d


for x in range(174457, 174505+1):
    if len(f(x)) == 2:
        print(*f(x))
