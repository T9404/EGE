minc = float('inf')

for k in range(1, 1000):
    a = bin(k)[2:]

    if (k % 2 == 0):
        a += '01'
    else:
        a += '10'
        
    if (int(a, 2)) > 97:
        minc = min(minc, k)

print(minc)
