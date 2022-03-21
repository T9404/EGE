def prime(x):
    return all(x % i != 0 for i in range(2, int(x**0.5)+1))


def f(x):
    a = set()

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)
            
    b = list(a)
    b = [i for i in b if prime(i)]

    if 400 < len(a) < 440 and len(b) >= 1:
        return max(b)
    else:
        return 0


for i in range(5000000, 10000000+1):
    if i % 180 == 0:
        if f(i):
            print(i, f(i))
