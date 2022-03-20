from functools import lru_cache


def move(h):
    return h+1, h*2, h*3


@lru_cache(None)
def F(h):
    if h >= 36:
        if h <= 60:
            return 'W'
        else:
            return 'P1'

    if any(F(m) == 'W' for m in move(h)):
        return 'P1'
    if all(F(m) == 'P1' for m in move(h)):
        return 'V1'
    if any(F(m) == 'V1' for m in move(h)):
        return 'P2'
    if all(F(m) in ['P1', 'P2'] for m in move(h)):
        return 'V2'


t19 = [x for x in range(1, 36) if F(x) == 'V1']
print(min(t19))

t20 = [x for x in range(1, 36) if F(x) == 'P2']
print(len(t20))

t21 = [x for x in range(1, 36) if F(x) == 'V2']
print(min(t21), max(t21))
