from itertools import *

#Решение автора
al = 'плюсёнок'
sogl = 'плснк'
s = sorted(set([x for x in map(lambda x: ''.join(x), product(al, repeat=7)) if all(x[0] != f for f in sogl) and all('ё'+l not in x for l in sogl) and all(l+'ё' not in x for l in sogl)]))
print(len(s))



#Костыльное решение обывателя(маслёнка)
a = 'ПЛЮСЁНОК'
l_l = 'ПЛСНКЁ'
la = list(set(map(''.join, list(product(l_l, repeat=2)))))
la += list(set(map(''.join, list(product('ЁПЛСНК', repeat=2)))))
la = sorted(set([ x for x in la if ('Ё' in x) and ('ЁЁ' not in x)]))
k = 0
print(la)
for j in product(a, repeat=7):
    word = ''.join(j)
    if word[0] not in 'ПЛСНК':
        if all(la_w not in word for la_w in la):
            k+=1
print(k)
