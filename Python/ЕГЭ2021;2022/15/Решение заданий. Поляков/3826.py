def f(x, a):
    return  (a % 35 == 0) and (730 % x == 0) <= ( (a % x != 0) <= (110 % x != 0))


for a in range(1, 10000):
    flag = True
    for x in range(1, 1000):
        if not f(x, a):
            flag = False
            break
    if flag:
        print(a)
        break

