from itertools import *
print('>>>>>')
# №3540 К.Ю.Поляков
'''
Женя составляет слова переставляя буквы З, А, П, И, С, Ь. 
Сколько слов может составить Женя, если известно, 
что Ь не может стоять на первом месте и после гласной? 
'''
amount = 0
word = 'ЗАПИСЬ'
for i in permutations(word, r=6):
    s = ''.join(i)
    if s[0] != 'Ь' and 'АЬ' not in s and 'ИЬ' not in s:
        amount+=1
        #print(s)
print(amount)