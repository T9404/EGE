from itertools import *
i = 1
for x in product('АИМРЯ', repeat=4):
    s = ''.join(x)

    if s == 'АРИЯ':
        print(i)
        
    i+=1

