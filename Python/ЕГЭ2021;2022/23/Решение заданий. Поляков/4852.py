def fibonacci(x):
    if (x == 1) or (x == 2):
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

def f(s, e):
    if s > e: return 0
    elif s == e: return 1
    else:
        return f(s+1, e)+f(s+3, e)+f( fibonacci(s), e)
print(f(6, 21))
