for i in range(1, 100000):
    a = bin(i)[2:]
    a += a[len(a)-1]

    a += str(a.count('1') % 2)
    a += str(a.count('1') % 2)

    if (int(a, 2) > 144):
        print(int(a, 2))
        break
