start, end = 174457, 174505

for x in range(start, end + 1):
    div = []
    sq = int(x**0.5)

    if sq**2 == x:
        continue

    for d in range(2, sq):
        if x % d == 0:
            div += [d, x//d]

            if len(div) > 2:
                break

    if len(div) == 2:
        print(*div)
