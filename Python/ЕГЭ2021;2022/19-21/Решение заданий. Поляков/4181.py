from functools import lru_cache


def move(h):
    a, b = h
    return (sum(h), b), (a, sum(h))


@lru_cache(None)
def f(h):
    if sum(h) >= 45:
        return 'WIN'
    elif any(f(d) == 'WIN' for d in move(h)):
        return 'P1'
    elif all(f(d) == 'P1' for d in move(h)):
        return 'V1'
    elif any(f(d) == 'V1' for d in move(h)):
        return 'P2'
    elif all(f(d) in ['P1', 'P2'] for d in move(h)):
        return 'V2'


def f__19(h):
    if sum(h) >= 45:
        return 'WIN'
    elif any(f(d) == 'WIN' for d in move(h)):
        return 'P1'
    elif any(f(d) == 'P1' for d in move(h)):
        return 'V1'


answer_19 = min([s for s in range(1, 1000) if f__19((7, s)) == 'V1'])
print(answer_19)

answer_20 = [s for s in range(1, 1000) if f((6, s)) == 'P2']
print(min(answer_20), max(answer_20))

answer_21 = min([s for s in range(1, 1000) if f((s, s)) == 'V2'])
print(answer_21)
