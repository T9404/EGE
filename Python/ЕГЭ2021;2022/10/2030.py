f = open('10-j1.txt', encoding='utf8')

punctuation = r"""!"#$%&'()*+,./:;<=>?@[\]^_`{|}~""" # Без дефиса
words = []
while (s := f.readline()) != "":
    s = s.strip()
    for sp in punctuation:
        s = s.replace(sp, " ")
    words += [_ for _ in s.split()]
f.close()

c = 0

for w in ['я', 'Я']:
    c += words.count(w)

print(c)