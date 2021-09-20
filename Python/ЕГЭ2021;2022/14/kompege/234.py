x = 2 * 27 ** 7 + 3 ** 10 - 9
k = 0
while x:
    if x % 3 == 0:
        k+=1
    x //= 3
print(k)
