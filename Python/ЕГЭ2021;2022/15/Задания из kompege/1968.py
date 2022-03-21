d = range(17, 58+1)
c = range(29, 80+1)


def f(x, a1, a2):
    return (x in d) <= (((x not in c) and not(a1 <= x <= a2)) <= (x not in d))


m = float('inf')

for a1 in range(15, 85):
    for a2 in range(a1, 85):
        if all(f(x, a1, a2) == 1 for x in range(10, 6000)):
            if m > a2 - a1:
                m = a2 - a1
                start = a1
                end = a2

print(start, end)
print(m)

print('answer: ', 29 - start)
