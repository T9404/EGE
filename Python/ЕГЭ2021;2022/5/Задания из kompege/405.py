def f(x):
    x_2 = bin(x)[2:]
    if x % 2 == 0:
        x_2+= '01'
    else:
        x_2 += '10'
    return int(x_2, 2)

for i in range(1, 1000):
    if f(i) > 81:
        print(f(i))
        break
