from itertools import *


d = [''.join(i) for i in product('012345678', repeat=3) if len(set(i)) == 1]
k = 0

for i in product('012345678', repeat=7):
    w = ''.join(i)
    if w[0] not in '0246' and w[-3:] not in d:
        k += 1

print(k)
