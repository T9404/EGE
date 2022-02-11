def f(x):
    d = set()

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
            
    return d


for x in range(135790, 163228+1):
    arr = f(x)
    if sum(arr) > 460000:
        print(len(arr), sum(arr))
