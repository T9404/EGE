'''
Ксюша составляет слова, меняя местами буквы в слове МИМИКРИЯ. 
Сколько различных слов, включая исходное, может составить Ксюша?
'''
# https://prnt.sc/pMDzengID_ic


from itertools import permutations


unique = set(''.join(i) for i in permutations('МИМИКРИЯ', r=8))
print(len(unique))
