from functools import lru_cache


def move(h):
    ''' # /// 1) (+1)  /// 2) (*2) /// 3) (+3) '''
    a, b = h
    k = []

    if (b != 1):
        k.append((a+1, 1))
    if (b != 3):
        k.append((a+3, 3))
    if (b != 2):
        k.append((a*2, 2))

    return k


@lru_cache(None)
def F(h):
    a, b = h
    if (a >= 55):
        return 'W'
    if any(F(m) == 'W' for m in move(h)):
        return 'P1'
    if all(F(m) == 'P1' for m in move(h)):
        return 'V1'
    if any(F(m) == 'V1' for m in move(h)):
        return 'P2'
    if all(F(m) in ['P1', 'P2'] for m in move(h)):
        return 'V2'


t19 = [i for i in range(1, 55) if F((i, 0)) == 'V1']
print('19-', t19[0])

t20 = [i for i in range(1, 55) if F((i, 0)) == 'P2']
print('20-', min(t20), max(t20))

t21 = [i for i in range(1, 55) if F((i, 0)) == 'V2']
print('21-', t21[0])
