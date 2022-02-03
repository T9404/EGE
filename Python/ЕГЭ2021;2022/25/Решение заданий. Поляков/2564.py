start, end = 194455, 194500

for x in range(start, end + 1):
    div = []
    sq = int(x**0.5)

    if sq**2 == x:
        continue

    for d in range(1, sq):
        if x % d == 0:
            div += [d, x//d]

            if len(div) > 4:
                break
            
    if len(div) == 4:
        div.sort()
        print(*div[-2:])
