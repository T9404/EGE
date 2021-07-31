'''
(№ 4240) (А. Куканова) Даша составляет слова, меняя местами буквы
в слове ТИКТОК так, что любые две соседние буквы должны быть различны
между собой. Сколько слов, включая исходное, может составить Даша? 
'''



from itertools import permutations
a = []
word = 'ТИКТОК'


for i in permutations(word, r=6):
    w = ''.join(i)
    if ('ТТ' not in w) and ('КК' not in w):
        a.append(w)
            
        
a1 = list(set(a))
print(len(a1))
