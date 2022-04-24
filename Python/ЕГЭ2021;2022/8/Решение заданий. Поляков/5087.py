from itertools import product


k = 0

for i in product('ЕКЛОСТ', repeat=5):
    k += 1
    w = ''.join(i)

    if w[0] == 'С' and 'ОО' in w:
        print(k)
        break
