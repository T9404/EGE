d = range(170, 580+10)
c = range(290, 800+10)

def f(x, a1, a2):
    return (x in d) <= (( (x not in c) and not(a1 <= x <= a2)) <= (x not in d))

m = float('inf')
for a1 in range(150, 850):
    for a2 in range(a1+1, 850):
        if all( f(x, a1, a2) == 1 for x in range(10, 6000)):
            if m > a2 - a1:
                m = a2 - a1
                start = a1 / 10
                end = a2 / 10
    
print(start, end)
print(m/10) #Про округление смотрите в ".../15/Основные методы решения/Числовая прямая.py"
