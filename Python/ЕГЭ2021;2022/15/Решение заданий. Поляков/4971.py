q = range(40, 75+1)
p = range(25, 50+1)


def f(x, a1, a2):
    return (x in q) <= (((x in p) == (x in q)) or ((x not in p) <= (a1 <= x <= a2)))


mini = float('inf')


for a1 in range(1, 130):
    for a2 in range(a1, 130):
        if all(f(x, a1, a2) == 1 for x in range(1, 130)):
            if mini > a2 - a1:
                mini = a2 - a1
                start = a1
                end = a2

print(mini)
print(start, end)

print(' p ∈ [25, 50], q ∈ [40, 75]  ==> Ответ: ', end-50)
