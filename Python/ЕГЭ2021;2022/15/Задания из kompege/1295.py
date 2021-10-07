p = range(170, 540+10)
q = range(370, 830+10)

def f(x, a1, a2):
    return (x in p) <= ( ( ( x in q) and not( a1 <= x <= a2 ) ) <= (x not in p))

m = float('inf')
for a1 in range(100, 900):
    for a2 in range(a1+1, 900):
        if all( f(x, a1, a2) == 1 for x in range(10, 6000)):
            if m > a2-a1:
                z = a2 / 10
                c = a1 / 10
                m = a2-a1
print(c, z)
print(m/10) 



#Про округление смотрите в ".../15/Основные методы решения/Числовая прямая.py"
