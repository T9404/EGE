from itertools import *

d = [] 
for i in permutations('АИМР', r=4):
    for j in product('АИН', repeat=4):
        word = ''.join(i) + ''.join(j)
        d.append(word)
d.sort()

for i, elem in enumerate(d):
    if elem == 'МАРИАННА':
        print(i+1)
        break
