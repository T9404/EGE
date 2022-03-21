from itertools import product


k = 0

for i in product('01234', repeat=6):
    w = ''.join(i)
    if w[0] == '3':
        if int(w, 5) % 2 == 0:
            k += 1

print(k)
