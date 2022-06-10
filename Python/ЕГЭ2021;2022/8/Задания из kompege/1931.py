'''
Ксюша составляет слова, меняя местами буквы в слове МИМИКРИЯ. 
Сколько различных слов, включая исходное, может составить Ксюша?
'''
# https://prnt.sc/AhX2W1LzVTOQ


from itertools import permutations


# буквы повторяются, обертываем в set() 
d = [''.join(i) for i in set(permutations('МИМИКРИЯ'))]
print(len(d))
