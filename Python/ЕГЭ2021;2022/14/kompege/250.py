for x in range(40, 1, -1):
    if bin(x)[-4:] == '1011':
        print(x)
        break
