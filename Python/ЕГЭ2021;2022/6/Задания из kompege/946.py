k = 0

for i in range(1, 10000):
    s = i
    n = 3

    while (s * n < 243) and (n < 10000):
        s //= 3
        n *= 9
        
    if n == 27:
        k += 1

print(k)
