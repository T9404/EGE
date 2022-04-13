x = 9 ** 81 + 27 ** 729 - 4


x_9 = []

while x:
    x_9.append(x % 9)
    x //= 9


ans = [i for i in x_9 if ((i == 0) or (i == max(x_9)))]
print(len(ans))
