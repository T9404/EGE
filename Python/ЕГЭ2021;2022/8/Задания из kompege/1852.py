from itertools import product

K = 0
for x in product('ГЕПАРД', repeat=5):
    d = ''.join(x)
    if d[0] != 'А' and d[-1] != 'Е' and d.count('Г') == 1:
        K += 1
 
print(K)
