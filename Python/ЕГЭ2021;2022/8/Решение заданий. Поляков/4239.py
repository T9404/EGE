from itertools import permutations
c=set()
for i in permutations('МИМИКРИЯ',r=8):
    s=''.join(i)
    c.add(s)

print(len(c))