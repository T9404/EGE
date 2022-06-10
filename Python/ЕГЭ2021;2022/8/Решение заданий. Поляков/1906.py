'''
Из букв слова К О Р Т И К составляются 6-буквенные последовательности. 
Сколько можно составить различных последовательностей, если известно, что 
в каждой из них содержится не менее 3 согласных?
'''
# https://prnt.sc/Lq2fJuPxl8_x


from itertools import *


a = [''.join(i) for i in product('КОРТИК', repeat=6)]
a = set([word for word in a if (word.count('К') +
        word.count('Р') + word.count('Т') >= 3)])


print(len(a))
