def isPrime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def calc_s(n):
    divs = set()

    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if not isPrime(d):
                divs.add(d)
            if not isPrime(n // d):
                divs.add(n // d)

    if len(divs) == 0:
        return 0
    else:
        return sum(divs)


c = 0

for i in range(912_671, 1, -2):
    s = calc_s(i)

    if s != 0 and i % s == 0:
        print(i, s)
        c += 1
        
        if c == 5:
            break
