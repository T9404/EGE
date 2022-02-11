for a in range(1, 1000):
    ok  = 1
    for x in range(1, 1000):
        if  ( (a % 3 == 0) and ( (220 % x == 0) <= ( (a % x != 0) <= (550 % x != 0)))) == 0:
            ok = 0
            break
    if ok:
        print(a)
        break

