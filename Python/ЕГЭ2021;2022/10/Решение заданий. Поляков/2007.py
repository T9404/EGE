'''
С помощью текстового редактора определите, сколько раз, не считая сносок, 
встречается слово «портрет» или «Портрет» в тексте романа в стихах А.С. Пушкина 
«Евгений Онегин» (файл 10-0.docx). Другие формы слова «портрет», такие 
как «портреты», «портретами» и т.д., учитывать не следует. 
В ответе укажите только число.
'''
# https://prnt.sc/nRW9C6BO64cZ


from string import punctuation


f = open('10-0.txt', encoding='utf8')


words = []

while (s := f.readline()) != "":
    s = s.strip()

    for sp in punctuation:
        s = s.replace(sp, " ")

    words += [_ for _ in s.split()]


print(words.count('портрет') + words.count('Портрет'))
