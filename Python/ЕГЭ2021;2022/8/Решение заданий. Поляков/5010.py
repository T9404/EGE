from itertools import product


s = 'ПРЕПАРАТ'


d = [''.join(i) for i in product('ПРТ', repeat=2)]
d += [''.join(i) for i in product('ЕА', repeat=2)]


k = 0


for i in set(product(s, repeat=8)):
    w = ''.join(i)
    
    if any(d[j] in w for j in range(len(d))):
        if all(s.count(str(j)) == w.count(str(j)) for j in w):
            k += 1


print(k)
