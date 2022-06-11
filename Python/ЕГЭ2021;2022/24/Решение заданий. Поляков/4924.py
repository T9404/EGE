'''
Текстовый файл 24-197.txt содержит строку из заглавных латинских букв X, Y и Z, 
всего не более чем из 106 символов. Определите максимальное количество идущих 
подряд троек символов ZXY или ZYX.
'''
# https://prnt.sc/6FcaoBgqloGx


f = open('24.txt')
s = f.readline()


answer = 0


for i in range(len(s) - 2):
    if s[i:i+3] in ['ZXY', 'ZYX']:
        count = 1
        j = i + 3

        while (j + 2) <= len(s):
            if s[j:j+3] in ['ZXY', 'ZYX']:
                count += 1
                j += 3
            else:
                answer = max(answer, count)
                break


print(answer)
