def f(x):
    a = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)
    a.add(x)
    return sorted(a)
for x in range(154026, 154043+1):
    if len(f(x)) == 4:
        print(*f(x)[2:])
