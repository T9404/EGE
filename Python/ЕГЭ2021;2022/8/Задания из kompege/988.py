'''
Маша выписывает в алфавитном порядке буквенные комбинации длиной 4, составленные 
из букв М, А, Р, И, Я. На какой позиции от начала списка будет комбинация АРИЯ?  

Вот начало списка: 

1. АААА 
2. АААИ 
3. АААМ 
4. АААР 
5. АААЯ 
6. ААИА 
'''
# https://prnt.sc/hWxBdZgeplQ7


from itertools import *


i = 0
for i in product('АИМРЯ', repeat=4):
    i += 1
    word = ''.join(i)

    if word == 'АРИЯ':
        print(i)
