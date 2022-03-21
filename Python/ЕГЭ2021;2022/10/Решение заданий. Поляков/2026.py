from string import punctuation


f = open('10-0.txt', encoding='utf8')


words = []


while (s := f.readline()) != "":
    s = s.strip()

    for sp in punctuation:
        s = s.replace(sp, " ")
        
    words += [_ for _ in s.split()]


c = 0

for w in ['муж', 'Муж']:
    c += words.count(w)

print(c)
