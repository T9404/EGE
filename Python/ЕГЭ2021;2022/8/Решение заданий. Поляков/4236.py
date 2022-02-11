from itertools import permutations
c=0
for i in permutations('РЕЖИМДНО',r=6):
    s=''.join(i)
    if (s[0] in 'РЖМДН') and (s[1] in 'ЕИО') and (s[5] in 'ЕИО'):
        c+=1
print(c)