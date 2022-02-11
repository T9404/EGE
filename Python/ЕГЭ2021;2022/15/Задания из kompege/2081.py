from itertools import *
p = set([ '11'+''.join(x) for x in product('01', repeat=6) ])
q = set([''.join(x)+'0' for x in product('01', repeat=7) ])

def f(x, a):
    return (x not in a) <= ( ( x in p) or (x not in q) )

a = set()
for x in product('01', repeat=8):
    if not f(''.join(x), a):
        a.add(''.join(x))
print(len(a))
