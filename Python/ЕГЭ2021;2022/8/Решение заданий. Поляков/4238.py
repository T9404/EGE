from itertools import permutations


f = []

for x in permutations('ПЛСНЬ', r=3):
    s = ''.join(x)
    if (s[1] == 'Ь'):
        f.append(s)

c = 0

for x in permutations('АПЕЛЬСИН', r=7):
    s = ''.join(x)
    if any(k in s for k in f) or (s.count('Ь') == 0):
        c += 1

print(c)
