from functools import lru_cache

def move(h):
    return h+1, h*3

@lru_cache(None)
def f(h):
    if h >= 56 and h <= 80:
        return 'WIN'
    elif h > 80:  #ВНИМАНИЕ, ВНИМАНИЕ
        return 'P1'
    elif any( f(m) == 'WIN' for m in move(h)):
        return 'P1'
    elif all( f(m) == 'P1' for m in move(h)):
        return 'B1'
    elif any( f(m) == 'B1' for m in move(h)):
        return 'P2'
    elif all( f(m) == 'P2' or f(m) == 'P1' for m in move(h)):
        return 'V2'
for i in range(1, 55+1): 
    print(i, f(i))

# Продолжение внимания
'''   
В чем суть? Если мы вышли за 80, то победитель противник. Т.Е. кто еще был в игре
Как это отработать? Дело в том, что все наши ходы как бы смещаются, в этом случае на -1,
А это значит, что выигрывает ПРеДшественник. Но почему 'P1'? Все дело в том, что
мы делаем рекурсию и заканчиваем не на 'WIN', а на 'P1' (предшест) ...V1->P1->WIN, в нашем
случае: ...V1->P1  
'''
    
