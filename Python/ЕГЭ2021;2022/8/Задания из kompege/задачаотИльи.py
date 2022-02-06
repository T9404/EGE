'''
Человек составляет слова из букв ПИТОНЯГА, при чем гласная буква не может стоять в начале
слова и рядом с гласной. Буквы могут повторяться. Сколько слов может составить человек?
'''

from itertools import *


# Решение автора
s = 'ПИТОНЯГА'

permg = sorted(
    set([x for x in map(lambda x: ''.join(x), product(s[1::2], repeat=2))]))
s = sorted(set([x for x in map(lambda x: ''.join(x), product(s, repeat=8)) if all(
    x[0] != s[f] for f in range(1, len(s)+1, 2)) and all(g not in x for g in permg)]))

print(len(s))


# Решение простого обывателя
a = 'ПИТОНЯГА'
k = 0
la = list(set(map(''.join, list(product(a[1::2], repeat=2)))))

for i in product(a, repeat=8):
    word = ''.join(i)
    if word[0] not in a[1::2]:
        if all(la_w not in word for la_w in la):
            k += 1

print(k)
