x = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15**17 + 19*15**11 + 18338

x_15 = set()

while x:
    x_15.add(x % 15)
    x //= 15

print(len(x_15))
