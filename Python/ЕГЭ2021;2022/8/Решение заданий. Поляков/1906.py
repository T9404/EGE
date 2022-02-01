from itertools import *


a = [''.join(x) for x in product('КОРТИК', repeat=6)]
a = set([i for i in a if (i.count('К')+i.count('Р')+i.count('Т') >= 3)])

print(len(a))
