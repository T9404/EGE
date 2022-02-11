def f(s, e):
    if s > e:
        return 0
    elif s == e:
        return 1
    else:
        if s % 10 == 9: #мы можем себе такое позволить, поскольку числа 25 и 51 двузначные
            return f(s+1, e)+f(s+10, e)
        else:
            return f(s+1, e)+f(s+10+1, e)

print(f(25, 51))

