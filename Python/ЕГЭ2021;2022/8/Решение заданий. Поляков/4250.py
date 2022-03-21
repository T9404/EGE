from itertools import product


count = 0

for k in range(4, 7):
    for x in product('ОНИКС', repeat=k):
        s = ''.join(x)
        if (s.count('С') == 3) and (s.count('О') == 1):
            count += 1

print(count)
