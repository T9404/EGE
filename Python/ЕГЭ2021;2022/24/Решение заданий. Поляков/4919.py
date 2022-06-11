'''
Текстовый файл 24-191.txt содержит строку из заглавных латинских букв, всего не более чем 
из 106 символов. Определите количество подстрок длиной не менее 20 символов, которые начинаются 
буквой A, содержат ровно две буквы F, заканчиваются буквой B и не содержат других букв A и B, 
кроме первой и последней.
'''
# https://prnt.sc/1MpRHtwYgWKy


f = open('24.txt')
s = f.readline()


s = s.replace('A', 'A A', s.count('A')).replace('B', 'B B', s.count('B'))


array = [x for x in s.split() if (x[0] == 'A') and (x[len(x) - 1] == 'B') and (x.count('F')
         == 2) and (x.count('A') == 1) and (x.count('B') == 1) and (len(x) >= 20)]

print(len(array))
