b = range(180, 520+10)
c = range(160, 410+10)

def f(x, a1, a2):
    return ( ( x in b) <= (a1 <= x <= a2) ) and ( (x not in c) or (a1 <= x <= a2))

m = float('inf')

for a1 in range(150, 530):
    for a2 in range(a1+1, 530):
        if all( f(x, a1, a2) == 1 for x in range(100, 6000)):
            if m > a2- a1:
                m = a2-a1
                start = a1/10
                end = a2/10

print(start, end)
print(m/10)

#Про округление смотрите в ".../15/Основные методы решения/Числовая прямая.py"

