from itertools import *
k = 0

for x in product('AB123', repeat=8):
    word = ''.join(x)
    if word.count('A')+word.count('B') == 2:
        k+=1

print(k)
