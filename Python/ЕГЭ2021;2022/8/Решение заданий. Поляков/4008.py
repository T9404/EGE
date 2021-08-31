from itertools import *
print('>>>>>>>')
# №4008 К.Ю.Поляков
'''
Миша составляет 6-буквенные коды из букв Б, А, Л, О, Н. 
Каждая допустимая гласная буква может входить в код не более одного раза.
Сколько кодов может составить Миша? 
'''
count = 0
letter = 'БАЛОН'
for i in product(letter, repeat=6):
    j = ''.join(i)
    if j.count('А') <= 1 and j.count('О') <= 1:
        count+=1
print(count)