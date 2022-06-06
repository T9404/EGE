from itertools import *


k = 0

for i in product('0123456', repeat=7):
    w = ''.join(i)
    if w[0] not in '035' and (int('22' in w) + int('44' in w)) <= 1:
        k += 1

print(k)
