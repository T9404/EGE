from itertools import permutations

d = [''.join(x) for x in set(permutations('МИМИКРИЯ'))]
print(len(d))
