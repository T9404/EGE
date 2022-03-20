from itertools import product


count = 0
c = []

for x in product('АЗНС', repeat=5):
    s = ''.join(x)
    count += 1
    if (s == 'САЗАН') or (s == 'ЗАНАС'):
        c.append(count)

print(c[1]-c[0]+1)
