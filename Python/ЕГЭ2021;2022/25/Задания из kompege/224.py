def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return d

for x in range(333555, 777999+1):
    arr = f(x)
    up_ar = [i for i in arr if len(str(i)) == 2]
    if len(up_ar) == 35:
        print(min(up_ar), max(up_ar))
