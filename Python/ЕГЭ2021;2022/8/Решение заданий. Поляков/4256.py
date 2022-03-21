from itertools import permutations


s = 'КУСАТЬ'
k = 0

for i in permutations(s, r=5):
    j = ''.join(i)
    if j[0] != 'Ь' and 'СУК' not in j:
        if len(set(j)) == 5:
            k += 1

print(k)
