from string import punctuation


f = open('10-1.txt', encoding='utf8')


words = []


while (s := f.readline()) != "":
    s = s.strip()

    for sp in punctuation:
        s = s.replace(sp, " ")

    words += [_ for _ in s.split()]


c = 0

for w in [t for i in ('Я', 'Ты', 'Он', 'Она', 'Оно') for t in {i, i.lower()}]:
    c += words.count(w)

print(c)
