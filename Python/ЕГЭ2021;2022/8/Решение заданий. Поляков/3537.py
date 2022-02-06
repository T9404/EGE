from itertools import product


w = 'ЩОГБА'

for i, word in enumerate(product(w, repeat=6)):
    s = ''.join(word)
    if s == 'ОБЩАГА':
        print(i+1)
        break
