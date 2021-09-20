for i in range(21, 30):
    x = i
    x_3 = ''
    while x:
        x_3 += str(x % 3)
        x //= 3
    x_3 = x_3[::-1]
    if x_3[-2:] == '11':
        print(i)
