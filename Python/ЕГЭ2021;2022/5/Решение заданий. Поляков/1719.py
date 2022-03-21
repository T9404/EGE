from itertools import *


c = 0

for i in range(300, 401):
    a = set()

    for k in permutations(str(i), r=2):
        s = ''.join(k)
        if (s[0] != '0'):
            a.add(int(s))
            
    if (max(a)-min(a) == 20):
        c += 1

print(c)
