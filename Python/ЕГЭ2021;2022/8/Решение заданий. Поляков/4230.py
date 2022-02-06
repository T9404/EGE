# (№ 4230) (А. Куканова) Варя составляет пятизначные числа в шестнадцатиричной системе счисления, в которых цифры расположены в порядке неубывания.
# Сколько различных чисел может составить Варя?

from itertools import product


a = []

for i in range(0, 16):
    a.append(i)


def F(n):
    for i in range(len(n)-1):
        if (int(n[i+1]) < int(n[i])):
            return False
    return True


c = 0

for i in product(a, repeat=5):
    if (F(i) == True) and (i[0] != 0):
        c += 1
        #print(i)

print(c)
