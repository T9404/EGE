'''
С помощью текстового редактора определите, сколько раз, не считая сносок, 
встречается слово «супруг» в тексте романа в стихах А.С. Пушкина 
«Евгений Онегин» (файл 10-0.docx). Другие формы слова «супруг», 
такие как «супруга», «супругом» и т.д., учитывать не следует. 
В ответе укажите только число.
'''
# https://prnt.sc/ROnK7xHRsO2o


from string import punctuation


f = open('10-0.txt', encoding='utf8')


words = []

while (s := f.readline()) != "":
    s = s.strip()

    for sp in punctuation:
        s = s.replace(sp, " ")

    words += [_ for _ in s.split()]


count = 0
for w in ['супруг']:
    count += words.count(w)

print(count)
