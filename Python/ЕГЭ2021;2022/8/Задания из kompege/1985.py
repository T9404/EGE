'''
Петя составляет 8-буквенные слова из букв А, Б, И, К, О, Л, У, Н. 
Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить 
подряд две гласные или две согласные. Сколько различных кодов может составить Петя?
'''
# https://prnt.sc/q9enCOBzsTsr


from itertools import *


vowels = [''.join(x) for x in product('АИОУ', repeat=2)]
consonants = [''.join(i) for i in product('БКЛН', repeat=2)]

answer = 0


for i in permutations('АБИКОЛУН', r=8):
    word = ''.join(i)
    if (all(comb not in word for comb in vowels) and
            all(comb not in word for comb in consonants)):
        answer += 1


print(answer)
