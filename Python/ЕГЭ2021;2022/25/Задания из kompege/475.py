def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return max(d)

for x in range(224466, 664422+1):
    if all(x % i == 0 for i in [5, 7, 13]):
        if all(x % i != 0 for i in [25, 49, 169]):
            if f(x) < 100000 and f(x) % 100 == 19:
                print(x, f(x))
