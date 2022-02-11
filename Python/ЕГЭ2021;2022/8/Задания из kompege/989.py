from itertools import *
i = 0
for x in product('АИМРЯ', repeat=4):
    i+=1
    if i == 211:
        print(''.join(x))
