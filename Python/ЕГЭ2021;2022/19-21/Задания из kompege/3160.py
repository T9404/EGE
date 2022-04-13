from functools import lru_cache


def move(h):
    return h*2, h+2, h+1


@lru_cache(None)
def f(h):
    if h >= 22:
        return 'W'

    elif any(f(m) == 'W' for m in move(h)):
        return 'P1'
    elif all(f(m) == 'P1' for m in move(h)):
        return 'B1'
    elif any(f(m) == 'B1' for m in move(h)):
        return 'P2'
    elif all(f(m) == ['P1', 'P2'] for m in move(h)):
        return 'B2'
    elif any(f(m) == 'B2' for m in move(h)):
        return 'P3'
    elif all(f(m) in ['P1', 'P2', 'P3'] for m in move(h)):
        return 'B3'
    elif any(f(m) == 'B3' for m in move(h)):
        return 'P4'
    elif all(f(m) in ['P1', 'P2', 'P3', 'P4'] for m in move(h)):
        return 'B4'
    elif any(f(m) == 'B4' for m in move(h)):
        return 'P5'
    elif all(f(m) in ['P1', 'P2', 'P3', 'P4', 'P5'] for m in move(h)):
        return 'B5'


h_19 = [i for i in range(1, 21+1) if f(i) == 'B1']
print(*h_19)

h_20 = [i for i in range(1, 21+1) if f(i) == 'P2']
print(min(h_20), max(h_20))

h_21 = [i for i in range(1, 21+1) if f(i)[0] == 'B']
print(len(h_21))
