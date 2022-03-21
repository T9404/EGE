from functools import lru_cache


def move(h):
    a, b = h

    ans = []

    if a-1 > 0:
        ans.append((a-1, b))
    if b-1 > 0:
        ans.append((a, b-1))
    if a != 1:
        ans.append((int(a//2), b))
    if b != 1:
        ans.append((a, int(b//2)))

    return ans


@lru_cache(None)
def f(h):
    if sum(h) <= 18:
        return 'CP'
    elif any(f(m) == 'CP' for m in move(h)):
        return 'P1'
    elif all(f(m) == 'P1' for m in move(h)):
        return 'B1'
    elif any(f(m) == 'B1' for m in move(h)):
        return 'P2'
    elif all(f(m) in ['P1', 'P2'] for m in move(h)):
        return 'B2'


task_19 = [m for m in range(1, 50) if f((m, m)) == 'B1']
print(*task_19)

task_20 = [s for s in range(1, 50) if f((s, 13)) == 'P2']
print(task_20[0], task_20[-1])

task_21 = [n for n in range(1, 50) if f((n, n)) == 'B2']
print(min(task_21))
