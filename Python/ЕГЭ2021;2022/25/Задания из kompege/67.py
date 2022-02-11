def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(x//i)
            d.add(i)
    return d

for x in range(81234, 134689+1):
    if len(f(x)) == 3:
        print(*sorted(f(x)))
