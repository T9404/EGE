from itertools import *


k = 0
for x in product('ПУЛЯ', repeat=6):
    s = ''.join(x)
    if s.count('У') == 2:
        k += 1

print(k)
