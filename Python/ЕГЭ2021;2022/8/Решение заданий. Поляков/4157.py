'''
Сколько существует четных пятеричных чисел длиной 6, начинающихся с цифры 3?
'''
# https://prnt.sc/myebKDZesfYu


from itertools import product


count = 0


for i in product('01234', repeat=6):
    number = ''.join(i)
    if (number[0] == '3') and (int(number, 5) % 2 == 0):
        count += 1


print(count)
