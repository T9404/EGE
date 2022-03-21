from itertools import *


k = 0
for i in permutations('ИГРОК', r=5):
    s = ''.join(i)
    if s[0] != 'К' and 'РОК' not in s:
        k += 1
        
print(k)
