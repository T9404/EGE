'''
Ася составляет 7-буквенные слова из букв А, П, Е, Л, Ь, С, И, Н. 
Все буквы слова различны. Буква Ь, если встречается, стоит между двумя 
согласными. Сколько таких слов может составить Ася?
'''
# https://prnt.sc/2_COWtb_s8BY


from itertools import permutations


condition = [''.join(i) for i in permutations('ПЛСНЬ', r=3) if (i[1] == 'Ь')]
count = 0


for i in permutations('АПЕЛЬСИН', r=7):
    word = ''.join(i)
    if any(k in word for k in condition) or (word.count('Ь') == 0):
        count += 1


print(count)
