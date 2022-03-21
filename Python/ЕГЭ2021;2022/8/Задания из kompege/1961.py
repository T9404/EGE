from itertools import *


for i, x in enumerate(product('ЕЛМРУ', repeat=4)):
    if x[0] == 'Л':
        print(i+1)
        break
