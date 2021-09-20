for x in range(1, 100000000000000000000000000000):
    z = 36 ** 17 - 6 ** x + 71
    z_6 = ''
    while z:
        z_6 += str(z % 6)
        z //= 6
    if sum(map(int, z_6)) == 61:
        print(x)
        break
