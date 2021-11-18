from itertools import permutations

k = 0

for s in set(permutations('МАРИНА', r=6)):
    if s[0] not in 'АИ':
        k+=1

print(k)
