from itertools import permutations
c=set()
for i in permutations('ОДЕКОЛОН',r=8):
    s=''.join(i)
    if (not 'ОО' in s):
        c.add(s)

print(len(c))
