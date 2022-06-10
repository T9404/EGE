'''
Определите количество семизначных чисел, записанных в девятеричной системе 
счисления, учитывая, что числа не могут начинаться с цифр 2, 4 и 6 и не должны 
заканчиваться на тройку одинаковых цифр (например, на 000).
'''
# https://prnt.sc/m7dYc9i1Fsho


from itertools import product


d = [''.join(i) for i in product('012345678', repeat=3) if len(set(i)) == 1]

count = 0


for i in product('012345678', repeat=7):
    word = ''.join(i)
    if (word[0] not in '0246') and (word[-3:] not in d):
        count += 1


print(count)
