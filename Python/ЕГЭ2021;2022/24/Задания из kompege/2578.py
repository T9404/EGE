'''
Текстовый файл содержит строку из заглавных латинских букв и точек, всего не более 106 символов. 
Определите максимальное количество идущих подряд символов, среди которых нет точек, а количество 
гласных (букв A, E, I, O, U, Y) не превышает 7.
'''
# https://prnt.sc/yTGfFCE-VhxX


f = open('24.txt')
strin = f.readline()


array = strin.split('.')

mak = float('-inf')


for s in array:
    for i in range(len(s)):
        new_string = s[i]
        j = i + 1
        count_vowels = (new_string.count('A') + new_string.count('E') + new_string.count('I')
                        + new_string.count('O') + new_string.count('U') + new_string.count('Y'))

        while j < len(s):
            if (count_vowels == 7) and (s[j] in 'AEIOUY'):
                break
            else:
                new_string += s[j]
                j += 1

        mak = max(mak, len(new_string))


print(mak)
