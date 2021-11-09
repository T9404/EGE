k = 0

for i in range(1, 10000):
    d = i
    n = 20
    s = 40
    while (s + n < d) and (n > - 1000):
        s -= 10
        n -= 20
        
    if n > 0:
        k += 1

print(k)
