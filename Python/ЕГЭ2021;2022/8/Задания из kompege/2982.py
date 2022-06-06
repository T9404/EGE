from itertools import *


trash = [''.join(i) for i in product('02468ace', repeat=2)]  # регистр
trash += [''.join(i) for i in product('13579bdf', repeat=2)]
k = 0

for i in range(int('10000', 16), int('fffff', 16)):  # наименьшее и наибольшее возможное
    w = hex(i)[2:]
    if len(w) == len(set(w)) and all(elem not in w for elem in trash):
        k += 1

print(k)
