from itertools import *


letter = 'БАЛОН'
count = 0

for i in product(letter, repeat=6):
    j = ''.join(i)
    if ( j.count('А') <= 1 ) and ( j.count('О') <= 1 ):
        count += 1

print(count)
