def f(x):
    x_2 = bin(x)[2:]
    for _ in range(3):
        if x_2.count('1') == x_2.count('0'):
            x_2+=x_2[-1]
        else:
            if x_2.count('1') > x_2.count('0'):
                x_2+='0'
            else:
                x_2+='1'
    return int(x_2, 2)

for x in range(81, 100):
    if f(x) % 4 == 0:
        print(x)
        break

        
    
