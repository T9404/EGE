def f(x):
    x_2 = bin(x)[2:]

    for i in range(2):
        ost = x_2.count('1') % 2
        x_2 += str(ost)
        
    return int(x_2, 2)


for i in range(1, 500):
    if f(i) > 80:
        print(f(i))
        break
