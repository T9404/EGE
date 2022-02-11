from itertools import *

k = 0
for i in product('КРЕСЛО', repeat=4):
    w = ''.join(i)
    if w[0] not in 'ЕО' and w[-1] not in 'КРСЛ':
        k+=1
print(k)
