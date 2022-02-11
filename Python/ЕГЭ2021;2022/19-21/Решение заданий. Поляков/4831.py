from functools import lru_cache

def move(e):
    new_h = []
    h, l = e  # h - heap(куча), l - last(последний) ход противника 
    if l != 1:
        new_h += [ ( h+1, 1 )] 
    if l != 2:
        new_h += [( h+2, 2)]
    if l != 3:
        new_h += [( h*3, 3)]
    return new_h
#print(move( (5, 1) )) тестовые данные

@lru_cache(None)
def f(e):
    h, l = e
    if h >= 140: return 'CP'
    elif any(f(m) == 'CP' for m in move(e)): return 'P1'
    elif all(f(m) == 'P1' for m in move(e)): return 'B1'
    elif any(f(m) == 'B1' for m in move(e)): return 'P2'
    elif all(f(m) in ['P1', 'P2'] for m in move(e)): return 'B2'

    
ans_19 = [i for i in range(1, 139+1) if f( ( i, -1)   ) == 'B1']
ans_20 = [i for i in range(1, 139+1) if f( (i, -1)) == 'P2' ]
ans_21 = [i for i in range(1, 139+1) if f( (i, -1)) == 'B2']

print(*ans_19)
print(min(ans_20), max(ans_20))
print(*ans_21)

