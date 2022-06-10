'''
Вася составляет слова из букв слова ПРЕПАРАТ. Код должен состоять из 8 букв, 
и каждая буква в нём должна встречаться столько же раз, сколько в заданном слове. 
Кроме того, в коде должны стоять рядом две гласные или две согласные буквы. 
Сколько различных слов может составить Вася?
'''
# https://prnt.sc/eXqVcMmVWjJg


from itertools import product


word = 'ПРЕПАРАТ'

d = [''.join(i) for i in product('ПРТ', repeat=2)]
d += [''.join(i) for i in product('ЕА', repeat=2)]

count = 0


for i in set(product(word, repeat=8)):
    w = ''.join(i)
    if (any(d[j] in w for j in range(len(d))) and
            all(word.count(str(j)) == w.count(str(j)) for j in w)):
        count += 1


print(count)
