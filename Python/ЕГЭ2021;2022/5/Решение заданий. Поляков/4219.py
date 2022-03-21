maxc = float('-inf')

for k in range(1, 10000):
    a = bin(k)[2:]

    if (k % 2 == 1):
        a += '11'
        a = '1'+a
    else:
        a += '00'
        a = '11'+a
        
    if (int(a, 2) < 127):
        maxc = max(maxc, int(a, 2))

print(maxc)
