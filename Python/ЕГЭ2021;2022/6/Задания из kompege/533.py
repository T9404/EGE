k = 0

for i in range(1, 1000000):
    d = i
    n = 27
    s = 12
    while s <= 2019:
        s += d
        n += 16
    if n == 171:
        k+=1

print(k)
