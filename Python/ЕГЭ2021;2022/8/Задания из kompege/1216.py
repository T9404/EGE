'''
Определите количество шестизначных чисел в пятеричной системе счисления, 
которые не оканчиваются цифрами 3 или 4 и не начинаются с цифры 1.
'''
# https://prnt.sc/aW69swzf3rIr


from itertools import product


def func(let):
    return (let[0] not in '01') and (let[-1] not in '34')


amount = 0


# пятеричная система счисления: 0, 1, 2, 3, 4
for i in product('01234', repeat=6):
    word = ''.join(i)
    if func(word):
        amount += 1


print(amount)
