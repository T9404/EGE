def f(a, x):
    return (70 % a == 0) and ((x % a != 0) <= ((x % 35 == 0) <= (x % 63 != 0)))


for a in range(5000, 1, -1):
    flag = True 

    for x in range(1, 10000):
        if not f(a, x):
            flag = False
            break
        
    if flag:
        print(a)
        break
