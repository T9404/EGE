from functools import lru_cache

def move(h):
    return h+1, h*2, h*3
@lru_cache(None)
def f(h):
    if 43 <= h <= 72:
        return 'CP'
    elif h > 72: return 'P1'
    elif any(f(m) == 'CP' for m in move(h)):
        return 'P1'
    elif all(f(m) == 'P1' for m in move(h)):
        return 'B1'
    elif any(f(m) == 'B1' for m in move(h)):
        return 'P2'
    elif all(f(m) in ['P1', 'P2'] for m in move(h)):
        return 'B2'

task_19 = min([ i for i in range(1, 42+1) if f(i) == 'B1' ])
print(task_19)
task_20 = len([i for i in range(1, 42+1) if f(i) == 'P2'])
print(task_20)
task_21 = ([i for i in range(1, 42+1) if f(i) == 'B2'])
print(task_21[0], task_21[-1])
