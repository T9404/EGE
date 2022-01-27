from itertools import product

k = 0
for i in product('0123456789', repeat=3):
    w = ''.join(i)
    if w[0] != '0':
        if int(w[0]) <= int(w[1]) <= int(w[2]):
            k +=1
print(k)
