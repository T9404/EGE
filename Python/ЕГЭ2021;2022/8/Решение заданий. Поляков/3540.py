from itertools import *


amount = 0
word = 'ЗАПИСЬ'

for i in permutations(word, r=6):
    s = ''.join(i)
    if s[0] != 'Ь' and 'АЬ' not in s and 'ИЬ' not in s:
        amount += 1

print(amount)
