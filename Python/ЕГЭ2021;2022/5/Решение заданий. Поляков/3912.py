minc = float('inf')

for k in range(101, 10000):
    a = bin(k)[2:]

    for _ in range(3):
        if (a.count('0') == a.count('1')):
            a += a[len(a)-1]
        else:
            if (a.count('0') < a.count('1')):
                a += '0'
            else:
                a += '1'
                
    if (int(a, 2) % 4 == 0) and (int(a, 2) % 8 != 0):
        minc = min(minc, k)

print(minc)
