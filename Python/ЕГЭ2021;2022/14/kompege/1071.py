def f(x, count=0):
    while x:
        if x % 5 == 4:
            count += 1
        x //= 5
    return count


for x in range(1, 1000):
    y = 125 ** 200 - 5 ** x + 74
    if f(y) == 100:
        print(x)
        break
