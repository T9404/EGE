for x in range(1, 100):
    try:
        if 68 % int('10', x) == 2:
            if int('1000', x) <= 68 <= int('10000', x):
                print(x)
                break
    except:
        continue
