def f(X, A):
    return (((X & 13 != 0) or (X & A == 0)) <= (X & 13 != 0)) or (X & A != 0) or (X & 39 == 0)


for a in range(1, 13*39+1):
    ok = True

    for x in range(1, (13*39+1)*10):
        if not f(x, a):
            ok = False
            break
        
    if ok == True:
        print(a)
        break
