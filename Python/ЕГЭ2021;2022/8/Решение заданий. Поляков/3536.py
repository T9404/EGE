from itertools import product


c = 0

for x in product('АКЛОШ', repeat=5):
    s = ''.join(x)
    if (s.count('О')+s.count('А') >= 1):
        c += 1

print(c)
