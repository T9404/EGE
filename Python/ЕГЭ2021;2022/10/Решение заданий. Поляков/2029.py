'''
С помощью текстового редактора определите, сколько раз, не считая сносок, 
встречаются личные местоимения (я, ты, он, она, оно), без учета 
регистра в тексте А.П. Чехова «Воры» (файл 10-1.docx). 
В ответе укажите только число.
'''
# https://prnt.sc/P5RWwKqVSQwQ


from string import punctuation


f = open('10-1.txt', encoding='utf8')


words = []

while (s := f.readline()) != "":
    s = s.strip()

    for sp in punctuation:
        s = s.replace(sp, " ")

    words += [_ for _ in s.split()]


count = 0
for w in [t for i in ('Я', 'Ты', 'Он', 'Она', 'Оно') for t in {i, i.lower()}]:
    count += words.count(w)

print(count)
