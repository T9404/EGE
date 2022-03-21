q = set(range(15, 30+1))
p = set(range(10, 25+1))
r = set(range(25, 40+1))


def f(x, a1, a2):
    return ((x in q) <= (x not in r)) and (a1 <= x <= a2) and (x not in p)


m = 0

for a1 in range(10, 45):
    for a2 in range(a1, 45):
        if all(f(x, a1, a2) == 0 for x in range(1, 100)):
            if a2-a1 > m:
                m = a2 - a1
                start = a1
                end = a2

print('answer: ', m)
print(start, end)
