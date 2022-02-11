for a in range(1, 7290+1):  # 45 * 162 = 7290
    good = True

    for x in range(1, 7290*100+1):
        if ((((x % a == 0) and (x % 45 == 0)) <= (x % 162 == 0)) and (a > 200)) == 0:
            good = False
            break
        
    if good:
        print(a)
        break
