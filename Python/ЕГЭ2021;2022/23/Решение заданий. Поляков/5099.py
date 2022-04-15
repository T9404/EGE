def f(s, e):
    if s > e: 
        return 0
    elif s == e:
        return 1
    else:
        if s % 2 != 0:
            return f(s*2, e)
        else:
            return f(s+1, e)+f(s+2, e)


print(f(2, 20)*f(20, 38)*f(38, 76))
