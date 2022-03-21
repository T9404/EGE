k = 0

def f(s, e, count):
    if (s > e):
        return 0
    elif s == e and count == 7:
        return 1
    elif s == e and count != 7:
        return 0
    else:
        return f(s+1, e, count+1)+f(s+4, e, count+1)+f(s*2, e, count+1)

print(f(3, 27, 0))
