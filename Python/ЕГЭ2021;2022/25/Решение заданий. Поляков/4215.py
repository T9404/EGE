def div(n):
    divs = set()

    for d in range(2, int(n**0.5)+1):
        if d == 8:
            continue

        if n % d == 0:
            if d % 10 == 8:
                divs.add(d)

            if (n//d) % 10 == 8:
                divs.add(n//d)

    if len(divs) == 0:
        return 0
    else:
        return min(divs)


c = 0

for i in range(500_001, 10**98):
    r = div(i)

    if r != 0:
        print(i, r)
        c += 1
        
        if c == 5:
            break
