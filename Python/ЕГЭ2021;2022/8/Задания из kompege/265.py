from itertools import *

i = 1
for x in product('АГИЛМОРТ', repeat=4):  # важен порядок символов
    if x[-2] == 'И' and x[-1] == 'М':
        answer = i
    i += 1

print(answer)
