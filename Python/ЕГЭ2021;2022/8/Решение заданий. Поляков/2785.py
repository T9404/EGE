from itertools import *

# Обозначу (↑, →, ↓, ←) как (0, 1, 2, 3) 
k = 0
for i in product('0123', repeat=4):
    w = ''.join(i)
    if w[0] != '0':
        if w[0] != w[2] and w[1] != w[3]:
            k += 1

print(k)
