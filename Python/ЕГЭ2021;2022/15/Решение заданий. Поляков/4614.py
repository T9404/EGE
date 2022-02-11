def f(x, a1, a2):
    return ( (5 <= x <= 110) <= (15 <= x <= 42)) or ( (not(a1 <= x <= a2)) <= (not(25 <= x <= 70)))

m = float('inf')

for a1 in range(1, 120):
    for a2 in range(a1+1, 120+1):
        if all( f(x, a1, a2) == 1 for x in range(1, 100)):
            if a2-a1 < m:
                m = a2 - a1
                start = a1
                end = a2

# Мы понимаем, что число 43 не может быть началом-концом отрезка, ближ число- 42. Поэтому end-42
print(end - (start-1))
