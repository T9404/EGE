for x in range(1, 10000):
    count = 0
    y = 4 ** 2015 + 2 ** x - 2 ** 2015 + 15

    while y:
        if y % 2 == 1:
            count += 1
        y //= 2
        
    if count == 500:
        print(x)
        break
