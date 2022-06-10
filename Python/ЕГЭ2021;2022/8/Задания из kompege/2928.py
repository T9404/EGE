'''
Определите количество семизначных чисел, записанных в семеричной системе 
счисления, учитывая, что числа не могут начинаться с цифр 3 и 5 и не должны 
содержать сочетания цифр 22 и 44 одновременно.
'''
# https://prnt.sc/TExq2aP3TL8o


from itertools import product


count = 0


for i in product('0123456', repeat=7):
    word = ''.join(i)
    if (word[0] not in '035') and ((int('22' in word) + int('44' in word)) <= 1):
        count += 1


print(count)
