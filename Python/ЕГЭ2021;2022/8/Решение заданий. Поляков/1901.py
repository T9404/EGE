'''
Сколько существует чисел, шестнадцатеричная запись которых 
содержит 3 цифры, причём все цифры различны и никакие 
две чётные и две нечётные цифры не стоят рядом.
'''
# https://prnt.sc/sw7DZj9oUF1b


from itertools import *


numbers = [''.join(i) for i in permutations(
    '0123456789abcdef', r=3) if (i[0] != '0')]


trash = [''.join(i) for i in product('02468ace', repeat=2)]
trash += [''.join(i) for i in product('13579bdf', repeat=2)]


answer = [numb for numb in numbers if all(comb not in numb for comb in trash)]

print(len(answer))
