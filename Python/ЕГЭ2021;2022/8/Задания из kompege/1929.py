'''
Ада составляет шестибуквенные слова из букв Д, Е, Й, К, С, Т, Р, А. 
Буква Й встречается в слове ровно один раз, и после неё обязательно идёт 
согласная. Буквы в слове не повторяются. Сколько слов может составить Ада?
'''
# https://prnt.sc/IArPuu816U-v


from itertools import permutations


values = ['ЙД', 'ЙК', 'ЙС', 'ЙТ', 'ЙР']
amount = 0


for i in set(permutations('ДЕЙКСТРА', r=6)):
    word = ''.join(i)
    if word.count('Й') == 1 and any(letter in word for letter in values):
        amount += 1


print(amount)
