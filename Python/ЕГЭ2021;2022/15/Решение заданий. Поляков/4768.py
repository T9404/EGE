def f(a1, a2, x):
    return (25 <= x <= 42) <= (  ( not(1 <= x <= 98) and (25 <= x <= 42)   )  <= (a1 <= x<=a2))

mini = float('inf')
for a1 in range(1, 100):
    for a2 in range(a1, 100):
        if all( f(a1, a2, x) == 1 for x in range(1, 100)):
            if mini > a2-a2:
                mini = a2 - a1
                start = a1
                end = a2

print(start, '-', end)
print('answer: ', mini)
