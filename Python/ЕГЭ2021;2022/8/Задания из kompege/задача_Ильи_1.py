'''
Человек составляет слова из букв ПИТОНЯГА, при чем гласная буква не может стоять в начале
слова и рядом с гласной. Буквы могут повторяться. Сколько слов может составить человек?
'''


# Решение автора

from itertools import *


s = 'ПИТОНЯГА'

permg = sorted(
    set([x for x in map(lambda x: ''.join(x), product(s[1::2], repeat=2))]))
s = sorted(set([x for x in map(lambda x: ''.join(x), product(s, repeat=8)) if all(
    x[0] != s[f] for f in range(1, len(s)+1, 2)) and all(g not in x for g in permg)]))

print(len(s))





# Решение простого обывателя


word = 'ПИТОНЯГА'
condition = list(set(map(''.join, list(product(word[1::2], repeat=2)))))

amount = 0


for i in product(word, repeat=8):
    word = ''.join(i)
    if word[0] not in word[1::2] and all(part not in word for part in condition):
        amount += 1


print(amount)
