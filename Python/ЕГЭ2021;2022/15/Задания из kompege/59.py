def f(a, x):
    return ((x % a == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0)


for a in range(1, 1000):
    flag = True
    
    for x in range(1, 1000):
        if not f(a, x):
            flag = False
            break

    if flag == 1:
        print(a)
        break
