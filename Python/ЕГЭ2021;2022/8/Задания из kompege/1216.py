from itertools import *


def f(x):
    if x[0] not in '01':
        if x[-1] not in '34':
            return True
    return False


k = 0
for i in product('01234', repeat=6):  # 5ная С.С.!!
    w = ''.join(i)
    if f(w):
        k += 1


print(k)
