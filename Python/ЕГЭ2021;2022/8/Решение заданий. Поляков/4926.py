from itertools import product


d = [''.join(i) for i in product('012345678', repeat=2) if len(set(''.join(i))) == 1]
k = 0

for i in product('012345678', repeat=7):
    w = ''.join(i)
    if w[0] not in '037':
        if all(j not in w for j in d):
            k += 1

print(k)