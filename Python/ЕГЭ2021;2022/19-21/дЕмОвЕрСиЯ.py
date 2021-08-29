def f(s): # ходы
    return s+1,  s*2
def win(s): # определение победы
    return s >= 29
z = {s for s in range(1, 29) } #все значения кучи

p1 = {s for s in z if any(win(t)  for t in f(s)) } #если попадаем в победу, Петя1

z -= p1 #вычитаем позиции, чтобы из них не ходить

v1 = {s for s in z if all(t in p1 for t in f(s)) } #всеми ходами попадаем в Петя1, значит Ваня1
print(*sorted(v1)) 
z -= v1 # не ходим повторно в позиции 

p2 = {s for s in z if any(t in v1 for t in f(s)) } # Попадаем в ВАня1 - мы Петя2
print(*sorted(p2))
z -= p2 #пиу-пам


v2 = {s for s in z if all(t in p1|p2 for t in f(s))} #попадаем в p1 или p2 ( " | " )
print(*sorted(v2))
z -= v2


