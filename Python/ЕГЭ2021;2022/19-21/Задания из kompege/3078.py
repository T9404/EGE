def move(e):
    h, b = e

    stones = []

    if b == 0:
        stones.append((h, 1))

    stones.append((h+2, b))
    stones.append((h*2, b))

    return stones


def f(h):
    a, b = h

    if a >= 20:
        return 'WIN'

    elif any(f(m) == 'WIN' for m in move(h)):
        return 'P1'

    elif all(f(m) == 'P1' for m in move(h)):
        return 'V1'

    elif any(f(m) == 'V1' for m in move(h)):
        return 'P2'

    elif all(f(m) in ['P1', 'P2'] for m in move(h)):
        return 'V2'

    elif any(f(m) == 'V2' for m in move(h)):
        return 'P3'

    elif all(f(m) in ['P1', 'P2', 'P3'] for m in move(h)):
        return 'V3'


def f_19_task(h):
    a, b = h

    if a >= 20:
        return 'WIN'

    elif any(f(m) == 'WIN' for m in move(h)):
        return 'P1'

    elif any(f(m) == 'P1' for m in move(h)):
        return 'V1'


ans_19 = min(i for i in range(1, 19+1) if f_19_task((i, 0)) == 'V1')
print(ans_19)

ans_20 = sorted(i for i in range(1, 19+1) if f((i, 0)) == 'P2')[-2:]
print(*ans_20)

ans_21 = (i for i in range(1, 19+1) if f((i, 0))[0] == 'V')
print(*ans_21)
