'''
Аня составляет трёхзначные числа в десятичной системе счисления, 
в которых цифры расположены в порядке неубывания. 
Сколько различных чисел может составить Аня?
'''
# https://prnt.sc/4h_6OGoCSzCh


from itertools import product


count = 0


for j in product('0123456789', repeat=3):
    if (j[0] != '0') and (j[0] <= j[1] <= j[2]):
        count += 1


print(count)
