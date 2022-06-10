''' 
Найдите минимальное значение переменной s, при вводе которого программа выведет число 30.
'''
# https://prnt.sc/dX4edPa3Ll5c


for i in range(-1000, 100000):
    s = i
    s = (s + 31) // 26
    n = 813

    while s > 0:
        n //= 3
        s -= n

    if n == 30:
        print(i)
        break
