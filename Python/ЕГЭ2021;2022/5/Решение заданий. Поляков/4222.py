maxc = float('-inf')

for k in range(1, 10000):
    a = hex(k//2)[2:]

    if (k % 4 != 0):
        a += 'f'
        a = 'a0'+a
    else:
        a += 'c'
        a = '15'+a
        
    if (int(a, 16) < 65536):
        maxc = max(maxc, k)

print(maxc)
