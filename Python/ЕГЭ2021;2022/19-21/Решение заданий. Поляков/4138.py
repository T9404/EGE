from functools import lru_cache


def move(h):
    if h > 0:

        if h % 2 == 0 and h % 3 == 0:
            return h//2, h-int(h*2//3)

        elif h % 2 != 0 and h % 3 == 0:
            return h-2, h - int(h*2//3)

        elif h % 2 == 0 and h % 3 != 0:
            return h//2, h-3
            
        else:
            return h-2, h-3


'''
Задача 19. Найти Ваню, если Петя делает неправильный ход, хотя должен выиграть
Это значит, что сам Ваня делает удачный ход и выигрывает(для нашего кода).
'''


@lru_cache(None)
def f19(h):
    if h == 1:
        return 'win'
    elif any(f19(m) == 'win' for m in move(h)):
        return 'B1'


B1 = 0
for i in range(1, 37+1):
    if f19(i) == 'B1':
        B1 = max(B1, i)
print(B1)


'''
Задачи 20-21 стандартно. 
'''


@lru_cache(None)
def f(h):
    if h == 1:
        return 'win'
    elif any(f(m) == 'win' for m in move(h)):
        return 'P1'
    elif all(f(m) == 'P1' for m in move(h)):
        return 'B1'
    elif any(f(m) == 'B1' for m in move(h)):
        return 'P2'
    elif all(f(m) in ['P1', 'P2'] for m in move(h)):
        return 'B2'


# 20
P2_min, P2_max = float('inf'), 0
for i in range(1, 37+1):
    if f(i) == 'P2':
        P2_min = min(i, P2_min)
        P2_max = max(i, P2_max)
print(P2_min, P2_max)

# 21
print(min([i for i in range(1, 37+1) if f(i) == 'B2']))
