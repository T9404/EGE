from itertools import product


c = 0

for i in range(4, 7):
    for k in product('ЧОАНИМЕ', repeat=i):
        s = ''.join(k)
        if (s.count('М') == 3):
            c += 1

print(c)
