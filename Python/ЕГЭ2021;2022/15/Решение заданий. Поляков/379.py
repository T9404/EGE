d = [a for a in range(1, 1000) if all(((x & 29 != 0) <= (
    (x & 12 == 0) <= (x & a != 0))) == 1 for x in range(0, 1000))]

print(min(d))
