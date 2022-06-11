'''
Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, 
всего не более 106 символов. Определите максимальное количество идущих подряд символов, 
среди которых нет гласных букв (символов A, E, I, O, U, Y), но есть не менее 6 точек.
'''
# https://prnt.sc/KOkYp2thVnFm


f = open('24.txt')
s = f.readline()


elements = ['A', 'E', 'I', 'O', 'U', 'Y']

for i in elements:
    s = s.replace(i, ' ')


max_strin = 0


for line in s.split():
    if line.count('.') >= 6:
        max_strin = max(max_strin, len(line))


print(max_strin)
