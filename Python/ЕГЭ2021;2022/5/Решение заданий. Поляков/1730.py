count = 0

for k in range(1, 10000):
    a = bin(k)[2:]

    for k in range(2):
        if (a.count('1') % 2 == 1):
            a += '1'
        else:
            a += '0'
            
    if (int(a, 2) < 100):
        count += 1

print(count)
