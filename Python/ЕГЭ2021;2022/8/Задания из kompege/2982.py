'''
Сколько существует чисел, шестнадцатеричная запись которых содержит 5 цифр, 
причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
# https://prnt.sc/QA3pZVZSzE2t


from itertools import *


# обращаем внимание на регистр
trash = [''.join(i) for i in product('02468ace', repeat=2)]
trash += [''.join(i) for i in product('13579bdf', repeat=2)]

amount = 0


# наименьшее и наибольшее возможное значение перебора
for i in range(int('10000', 16), int('fffff', 16)):
    number = hex(i)[2:]
    if len(number) == len(set(number)) and all(elem not in number for elem in trash):
        amount += 1


print(amount)
