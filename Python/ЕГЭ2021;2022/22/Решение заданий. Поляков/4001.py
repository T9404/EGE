for i in range(61//3+1, 10**9):  # нижняя граница перебора такая, чтоб b был положительным
    x = i
    a = 3 * x + 67
    b = 3 * x - 61

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    if a == 64:
        print(i)
        break
