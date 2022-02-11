def f(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        # потыкайте на калькуляторе и поймите почему *2, *2+1
        return f(s+1, e)+f(s*2, e)+f(s*2+1, e)


print(f(int('100', 2), int('11101', 2)))
