from itertools import product
k = 0
for x in product('0123456789', repeat=3):
    if x[0] != '0':
        if x[0] <= x[1] <= x[2]:
            k+=1
print(k)
