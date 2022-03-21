def isPrime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def calc_f(n):
    divs = set()

    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if isPrime(d):
                divs.add(d)
            if isPrime(n // d):
                divs.add(n // d)

    if len(divs) == 0:
        return 0
    else:
        return sum(divs) // len(divs)


c = 0


for i in range(650_001, 10 ** 965):
    f = calc_f(i)

    if f != 0 and f % 37 == 23:
        print(i, f)
        c += 1
        
        if c == 4:
            break
