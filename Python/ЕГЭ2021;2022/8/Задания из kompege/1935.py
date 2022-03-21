from itertools import permutations


k = 0
for x in set(permutations('ВАЙФУ', r=4)):
    s = ''.join(x)
    if s[0] != 'Й':
        if ('ВФ' not in s) and ('ФВ' not in s):
            k += 1

print(k)
