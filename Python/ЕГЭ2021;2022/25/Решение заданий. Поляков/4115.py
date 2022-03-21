def calc_s(n):
    divs = set()

    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)

    if len(divs) == 0:
        return 0
    else:
        return sum(divs)


c = 0


for i in range(150_001, 10 ** 965):
    s = calc_s(i)

    if s != 0 and s % 13 == 10:
        print(i, s)
        c += 1
        
        if c == 7:
            break
