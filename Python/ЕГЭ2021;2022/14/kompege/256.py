def f(x):
    x_6 = ''
    x_5 = ''
    y = x
    while x:
        x_6 += str(x % 6)
        x //= 6
    while y:
        x_5 += str(y % 5)
        y //= 5
    if len(x_6) == 2 and len(x_5) == 3:
        return True
    else: return False
for x in range(1, 10000):
    if x % 11 == 1:
        if f(x):
            print(x)
    
