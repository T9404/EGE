from itertools import *


k = 0

for i in product('ЯСНОВИДЕЦ', repeat=5):
    w = ''.join(i)
    if w[0] in 'СНВДЦ' and w[-1] in 'ЯОИЕ':
        if w.count(w[0]) == 1 and w.count(w[-1]) == 1:
            k += 1

print(k)
