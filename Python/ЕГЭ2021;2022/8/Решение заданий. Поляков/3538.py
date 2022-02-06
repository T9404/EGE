from itertools import *

write = 'АВДПР'  # В этом задании важен порядок кодировки символов, А-1, В-2, Д-3, П-4, Р-5

for i, word_i in enumerate(product(write, repeat=4)):
    u = ''.join(word_i)
    if len(set(u)) == 4 and 'А' not in u:
        print(u, i+1)
        break
