def factor(x):
    x+=1 # следующее число из условия
    a = set(range(2, x+1))
    n = 1
    for i in a:
        n*= i
    return n

#print(factor(3)) #тестовые

def f(s, e):
    if s > e or s == 12:
        return 0
    elif s == e:
        return 1
    else:
        return f(s+1, e)+f(s+4, e)+f( factor(s), e)
    
print(f(2, 24))
