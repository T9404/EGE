from itertools import *


d = [''.join(i) for i in product('ШРЛТН', repeat=2)]
d += 'AA'

k = 0


for i in set(permutations('ШАРЛАТАН', r=8)):
    w = ''.join(i)
    if any(j in w for j in d):
        k += 1


print(k)
