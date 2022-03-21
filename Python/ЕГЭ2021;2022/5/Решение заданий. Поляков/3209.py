def f(x):
    x_2 = bin(x)[2:]
    x_2 += x_2[-2]
    x_2 += x_2[1]

    return int(x_2, 2)


k = 0

for x in range(2, 1000000):
    if 100 <= f(x) <= 150:
        k += 1
        
print(k)
