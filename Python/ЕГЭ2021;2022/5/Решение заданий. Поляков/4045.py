count = 0

for k in range(1, 10000):
    a = k

    if (a % 2 == 0):
        a = a//2
    else:
        a = a-1


    if (a % 5 == 0):
        a = a//5
    else:
        a = a-1


    if (a % 7 == 0):
        a = a//7
    else:
        a = a-1

    if (a == 6):
        count += 1


print(count)
