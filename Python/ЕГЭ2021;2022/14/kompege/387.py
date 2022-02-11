x = 51 * 7 ** 12 - 7 ** 3 - 22

x_7 = ''
while x > 0:
    x_7 += str(x % 7)
    x //= 7

print(sum(map(int, x_7)))
