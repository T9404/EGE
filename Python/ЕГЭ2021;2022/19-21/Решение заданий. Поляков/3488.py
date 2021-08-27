from functools import lru_cache
from itertools import product

def move(h):
    a, b = h
    return (a+2, b), (a, b+2), (a*3, b), (a, b*3)

@lru_cache(None)
def f(h):
    new  = lambda *values: (f(m) in values for m in move(h))
    if sum(h) >= 45:
        return 'win'
    if any(new('win')):
        return 'P1'
    if all(new('P1')):
        return 'V1'
    if any(new('V1')):
        return 'P2'
    if all(new('P1', 'P2')):
        return 'V2'
k19 = 0
for k, s in product(range(1, 43+1), repeat=2):
        if (k+s) <= 43 and ( f((k, s)) == 'V1'):
                k19+=1
print(k19)
#Вы дождались задачи, где не нужно в 19 писать any)
'''
Найдите количество решений, при котором Ваня выигрывает первым ходом при
любых П1. действиях. Т.Е. all(P1 move)
'''
print(min([i for i in range(1, 43+1) if f((4, i)) == 'P2']), end=' ') 
print(max([i for i in range(1, 43+1) if f((4, i)) == 'P2' and (4 + i <= 43)]))
#лол, что. ты снова запускаешь перебор? п-производительность
print(max(i for i in range(1, 43+1) if (f((13, i)) == 'V2' and (13+i <= 43)))) #max для вывода написал
