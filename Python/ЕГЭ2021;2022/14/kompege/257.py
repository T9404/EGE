for x in range(1, 10000):
    if int('10', 7) <= x <= int('100', 7):
        if int('100', 6) <= x <= int('1000', 6):
            if x % 13 == 3:
                print(x)
