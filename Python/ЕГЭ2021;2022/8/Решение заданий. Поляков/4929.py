from itertools import product


d = [str(i) * 3 for i in '012345678']


k = 0


for i in product('012345678', repeat=7):
    w = ''.join(i)

    if w[0] not in '0246' and w[-3:] not in d:  # с нуля число не начинается
        k += 1


print(k)
