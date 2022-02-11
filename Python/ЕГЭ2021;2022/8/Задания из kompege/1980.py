from itertools import *


def f(d):
    for i in d:
        if i in 'WXYZ':
            return False
    return True


k = 0
for i in product('ABCWXYZ', repeat=6):
    d = ''.join(i)
    if d[-1] in 'WXYZ' and d[0] in 'WXYZ':
        if f(d[1:-1]):
            k += 1
            
print(k)
