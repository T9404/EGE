'''
Решим простую задачу. Цель не решить ее, а показать как себя застраховать.

1) Используем кэширование ( lru_cache() )

2) Сделать предел рекурсии:
import sys; sys.setrecursionlimit(value);  

3) Делать дополнительный счетчик. В методе Вадима он мне очень понравился. 

Применяем:
'''
import sys
from functools import lru_cache

def move(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*4, b), (a, b*4)

sys.setrecursionlimit(1500)
@lru_cache(None) 



def f(h, k): #код для 19 номера
    if sum(h) >= 105:
        return 'CP'
    if k > 100: #если уходит в бесконечную рекурсию - ливнуть с нее. Для этого мы передаем счетчик: f(кучи, счетчик) 
        return #переиграл
    
    joke = lambda *numbers: (f(m, k+1) in numbers for m in move(h)) #+1, т.к. мы делаем след ход
    if any(joke('CP')): return 'P1'
    if any(joke('P1')): return 'B1'
print(min([x for x in range(1, 100+1) if f((4, x), 0) == 'B1'])) 

