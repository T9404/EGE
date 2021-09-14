from itertools import *
k = 0

for x in product('ВИШНЯ', repeat=6):
    s = ''.join(x)
    if s.count('В') <= 1:
        if s[0] != 'Ш':
            if s[-1] not in 'ИЯ' and s[4:] != 'ИЯ':
                k+=1


print(k)
