p = range(5, 20+1)
q = range(15, 25+1)
r = range(35, 50+1)


def f(x, a1, a2):
    return ((x in p) <= (x in q)) or ((not(a1 <= x <= a2)) <= (x not in r))


mini = float('inf')


for a1 in range(1, 60):
    for a2 in range(a1, 60):
        if all(f(x, a1, a2) == 1 for x in range(1, 60)):
            if mini > a2 - a1:
                mini = a2 - a1
                start = a1
                end = a2


print(start, end)
print('answer: ', mini)
