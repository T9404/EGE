from itertools import product

word = 'АОУ'

for i, s in enumerate(product(word, repeat=5)):
    if i+1 == 240:
        print(''.join(s))

        
