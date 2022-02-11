from itertools import *
k = 0

d = [ ''.join(x) for x in product('АИОУ', repeat=2) ] #подряд гласные
z = [''.join(i) for i in product('БКЛН', repeat=2) ] #подряд согласные


for i in permutations('АБИКОЛУН', r=8):
    s = ''.join(i)
    if all(comb not in s for comb in d):
        if all(comb not in s for comb in z):
            k+=1
print(k)
