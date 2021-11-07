def f(x):
    x_2 = bin(x)[2:]
    if x % 2 == 0:
        x_2 = '1' + x_2 + '0'
    else:
        x_2 = '11'+x_2+'11'
    return int(x_2, 2)

#print(f(13))
m = float('inf')
for i in range(1, 1000):
    if f(i) > 52:
        m = min(f(i), m)
print(m)
        
