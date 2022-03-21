from itertools import product


k = 0

for j in product('ЗЕРКАЛО', repeat=6):
    word = ''.join(j)
    if word.count('К'):
        if word.count('К') <= 4:
            if len(set(word)) == len(word) - word.count('К') + 1:
                k += 1

print(k)
