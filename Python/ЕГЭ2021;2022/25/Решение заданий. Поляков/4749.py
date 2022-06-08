def f(n):
    a = set()

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            a |= {i, n//i}

    if len(a) < 3:
        return False
    else:
        return sum(sorted(a)[-3:])


def check(a):
    for i in range(len(a)-1):
        if int(a[i]) > int(a[i+1]):
            return False
    return True


i, k = 10_000_000, 0


while k < 5:
    i += 1
    s = f(i)

    if s:
        d = list(str(s))
        if check(d):
            k += 1
            print(s)
