'''
(№ 4240) (А. Куканова) Даша составляет слова, меняя местами буквы
в слове ТИКТОК так, что любые две соседние буквы должны быть различны
между собой. Сколько слов, включая исходное, может составить Даша? 
'''

''' Обратите внимание, в этой задачи повторяются ТТ и КК'''

#1 Решение
from itertools import permutations
a = []
word = 'ТИКТОК'


for i in permutations(word, r=6):
    w = ''.join(i)
    if ('ТТ' not in w) and ('КК' not in w):
        a.append(w)
            
        
a1 = list(set(a))
print(len(a1))

#2 Решение
from itertools import permutations
a = []
word = 'ТИКТОК'

count = 0
for i in permutations(word, r=6):
    w = ''.join(i)
    if ('ТТ' not in w) and ('КК' not in w):
        count+=1
            
        
print(count//4)



