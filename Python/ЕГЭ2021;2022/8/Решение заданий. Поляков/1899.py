from itertools import *

condition_1 = [ ''.join(i) for i in product('0246', repeat=2)]
condition_2 = [ ''.join(i) for i in product('1357', repeat=2)]

k = 0
for i in permutations('01234567', r=7):
    w = ''.join(i)
    if w[0] != '0':
        if all( (j not in w) for j in condition_1):
            if all( (j not in w) for j in condition_2):
                k += 1
print(k)
