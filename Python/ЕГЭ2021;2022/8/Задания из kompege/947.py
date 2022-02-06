from itertools import *

k = 0
for x in product('ABCD', repeat=4):
    if x[0] <= x[1] <= x[2] <= x[3]:
        k += 1

print(k)
