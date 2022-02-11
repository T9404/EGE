def f(x):
    d = set()

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)

    z = sorted(d)

    if len(z) >= 2:
        for i in range(len(z)-1):
            if z[i]+100 != z[i+1]:
                return False
    else:
        return False

    return max(z)


for x in range(862346, 1056242+1):
    if f(x):
        print(x, f(x))
