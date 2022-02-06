maxc = 0

for k in range(1, 100000):
    a = bin(k)[2:]
    a += a[len(a)-2]
    a += a[1]
    
    if (int(a, 2) <= 128):
        maxc = max(maxc, k)

print(maxc)
