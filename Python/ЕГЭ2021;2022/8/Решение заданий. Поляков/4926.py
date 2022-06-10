'''
Определите количество семизначных чисел, записанных в девятеричной системе 
счисления, учитывая, что числа не могут начинаться с цифр 3 и 7 и не должны 
содержать пары соседних одинаковых цифр (например, 00).
'''
# https://prnt.sc/8PtDv5AyJ1s1


from itertools import product


d = [''.join(i) for i in product('012345678', repeat=2)
     if (len(set(''.join(i))) == 1)]

count = 0


for i in product('012345678', repeat=7):
    w = ''.join(i)
    if w[0] not in '037' and all(j not in w for j in d):
        count += 1


print(count)
